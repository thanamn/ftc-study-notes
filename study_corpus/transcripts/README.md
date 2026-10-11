# Lecture transcripts (Whisper, local)

Thai lecture recordings from MyCourseVille (Kaltura) transcribed locally with
**faster-whisper `large-v3`** on the RTX 4060. No captions existed on the source
clips, so these are the only transcripts.

## Files per lecture
- `FTCNN.md`  — timestamped Markdown (grouped ~1 min blocks)
- `FTCNN.srt` — subtitle file
- `FTCNN.jsonl` — one record per utterance (start, end, text)
- `FTCNN.log` — run log

## Chosen configuration (after benchmarking — see `_ab_turbo_report.md`)

```
large-v3 · float16 · batch 16 · beam 5 · 1 worker
```
- **Batching** is the key to speed: **0.4× → ~8× realtime** (the GPU sat idle
  between Python decode steps without it).
- **turbo rejected**: ~1.7× faster but mangles Thai badly.
- **int8_float16 rejected**: slower on this GPU.
- One worker only: a batched worker already uses ~7.9/8.2 GB and 100% util.

## Hard-audio handling (echoey lectures)
Echoey/reverberant rooms cause Whisper to (a) loop repetitively and (b) guess
English and hallucinate boilerplate.

Mitigations added to `transcribe.py`:
- `--no-repeat-ngram 3` — **cures the repetition loops**
- `--lang th` — **force Thai**, prevents English hallucination
- **no audio filtering at all** — tested: even *mild* `highpass/lowpass` made FTC01 worse (introduced garbage); raw audio wins

## Caveat
- **FTC01 — scrapped.** Audio too echoey; content is intro-level and fully
  covered by the slides (`../FTC01_Dependable_Computing.md`). No transcript kept.
- **FTC02** (also echoey) — best-effort; prefer the slides for anything exact.
- **FTC03–FTC07** (clean audio) — high quality, safe to rely on.
