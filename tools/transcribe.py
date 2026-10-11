"""
Transcribe one lecture audio file with faster-whisper and emit
timestamped Markdown + SRT + JSONL.

Usage:
    python transcribe.py <audio> <out_basename> [--model large-v3] [--lang auto]

Outputs: <out_basename>.md, <out_basename>.srt, <out_basename>.jsonl
"""
import os, sys, json, argparse, datetime

# Whisper weights live outside the project tree (kept out of the folder).
MODELS_DIR = os.environ.get("WHISPER_MODELS") or os.path.join(
    os.environ.get("LOCALAPPDATA", r"C:\Users\thana\AppData\Local"),
    "Temp", "opencode", "whisper_models")

# --- Make CUDA DLLs shipped by nvidia-* pip wheels visible to ctranslate2 ---
try:
    import sysconfig
    sp = sysconfig.get_paths().get("purelib")
    for sub in ("cublas", "cudnn", "cuda_nvrtc", "cuda_runtime"):
        b = os.path.join(sp, "nvidia", sub, "bin")
        if os.path.isdir(b):
            os.add_dll_directory(b)
            os.environ["PATH"] = b + os.pathsep + os.environ["PATH"]
except Exception as e:
    print("DLL path setup warning:", e)

from faster_whisper import WhisperModel
import wave, numpy as np

def load_wav_mono16k(path):
    """Read a 16 kHz mono PCM WAV into a float32 array, bypassing PyAV."""
    with wave.open(path, "rb") as w:
        fr, ch, sw, n = w.getframerate(), w.getnchannels(), w.getsampwidth(), w.getnframes()
        raw = w.readframes(n)
    if fr != 16000:
        raise ValueError(f"expected 16 kHz audio, got {fr}")
    if sw == 2:
        a = np.frombuffer(raw, dtype="<i2").astype(np.float32) / 32768.0
    elif sw == 4:
        a = np.frombuffer(raw, dtype="<i4").astype(np.float32) / 2147483648.0
    else:
        raise ValueError(f"unsupported sample width {sw}")
    if ch > 1:
        a = a.reshape(-1, ch).mean(axis=1)
    return np.ascontiguousarray(a)

def ts(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = int(t % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def srt_ts(t):
    h = int(t // 3600); m = int((t % 3600) // 60)
    s = int(t % 60); ms = int((t - int(t)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio")
    ap.add_argument("out")
    ap.add_argument("--model", default="large-v3")
    ap.add_argument("--lang", default=None, help="'auto' or a code like th/en")
    ap.add_argument("--compute", default=None, choices=["float16", "int8_float16"],
                    help="GPU precision. int8_float16 halves VRAM (enables 2 parallel workers).")
    ap.add_argument("--batch", type=int, default=0,
                    help=">0 enables batched inference (much faster, more VRAM).")
    ap.add_argument("--beam", type=int, default=5,
                    help="beam size; 1 = greedy (fastest), 5 = default (accurate).")
    ap.add_argument("--no-repeat-ngram", type=int, default=0,
                    help="block repeating n-grams (e.g. 3) — cures degeneration loops.")
    ap.add_argument("--repetition-penalty", type=float, default=1.0,
                    help=">1 penalises repeated tokens (e.g. 1.1).")
    ap.add_argument("--allow-cpu", action="store_true",
                    help="Fall back to CPU if GPU fails (slow; off by default to avoid surprises).")
    args = ap.parse_args()

    lang = None if (args.lang in (None, "", "auto")) else args.lang

    model = None
    cands = [("cuda", c) for c in ([args.compute] if args.compute else ["float16", "int8_float16"])]
    if args.allow_cpu:
        cands.append(("cpu", "int8"))
    for device, ctype in cands:
        try:
            print(f"Loading {args.model} on {device}/{ctype} ...", flush=True)
            model = WhisperModel(args.model, device=device, compute_type=ctype,
                                 download_root=MODELS_DIR)
            print(f"Using {device}/{ctype}", flush=True)
            break
        except Exception as e:
            print(f"  {device}/{ctype} failed: {e}", flush=True)
    if model is None:
        sys.exit("Could not load Whisper model on GPU (OOM?). Try --compute int8_float16.")

    audio_input = load_wav_mono16k(args.audio)
    print(f"Audio loaded: {len(audio_input)/16000/60:.1f} min", flush=True)

    common = dict(language=lang, vad_filter=True,
                  vad_parameters=dict(min_silence_duration_ms=700),
                  condition_on_previous_text=False,
                  no_repeat_ngram_size=args.no_repeat_ngram,
                  repetition_penalty=args.repetition_penalty)
    if args.batch and args.batch > 0:
        from faster_whisper import BatchedInferencePipeline
        pipe = BatchedInferencePipeline(model=model)
        segments, info = pipe.transcribe(audio_input, batch_size=args.batch,
                                         beam_size=args.beam, **common)
    else:
        segments, info = model.transcribe(
            audio_input, beam_size=args.beam,
            temperature=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
            word_timestamps=False, **common)
    print(f"Detected language: {info.language} (p={info.language_probability:.2f}), "
          f"duration={info.duration/60:.1f} min", flush=True)

    segs = []
    partial = open(args.out + ".partial.jsonl", "w", encoding="utf-8")
    for i, s in enumerate(segments, 1):
        rec = {"i": i, "start": round(s.start, 2), "end": round(s.end, 2),
               "text": s.text.strip()}
        segs.append(rec)
        partial.write(json.dumps(rec, ensure_ascii=False) + "\n")
        partial.flush()          # survive a kill mid-run
        if i % 50 == 0:
            print(f"  ...{i} segments ({ts(s.end)})", flush=True)
    partial.close()

    base = args.out
    with open(base + ".jsonl", "w", encoding="utf-8") as f:
        for s in segs:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")

    with open(base + ".srt", "w", encoding="utf-8") as f:
        for s in segs:
            f.write(f"{s['i']}\n{srt_ts(s['start'])} --> {srt_ts(s['end'])}\n{s['text']}\n\n")

    # group segments into ~1-minute blocks for readable Markdown
    with open(base + ".md", "w", encoding="utf-8") as f:
        f.write(f"# Transcript\n\n> language: {info.language} · "
                f"{info.duration/60:.1f} min · model {args.model}\n\n")
        block, block_start = [], None
        def flush():
            if block:
                f.write(f"**[{ts(block_start)}]** " + " ".join(block) + "\n\n")
        for s in segs:
            if block_start is None:
                block_start = s["start"]
            if s["start"] - block_start >= 60:
                flush(); block, block_start = [], s["start"]
            block.append(s["text"])
        flush()

    print(f"Done: {len(segs)} segments -> {base}.md/.srt/.jsonl", flush=True)

if __name__ == "__main__":
    main()
