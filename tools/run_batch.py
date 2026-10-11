"""
Transcribe every FTC*.wav not yet transcribed, with a bounded worker pool.

    python run_batch.py --workers 2 --compute int8_float16
    python run_batch.py --workers 2 --batch 8 --compute int8_float16

Each worker is a separate `transcribe.py` process; the GPU can hold ~2 of
large-v3 at int8_float16 in 8 GB.
"""
import os, sys, glob, argparse, subprocess, time

HERE = os.path.dirname(os.path.abspath(__file__))
# project root = parent when this script lives in tools/, else the script dir
ROOT = os.path.dirname(HERE) if os.path.basename(HERE).lower() == "tools" else HERE
AUDIO = os.environ.get("FTC_AUDIO_DIR") or r"C:\Users\thana\AppData\Local\Temp\opencode\ftc_audio"
OUTDIR = os.path.join(ROOT, "study_corpus", "transcripts")
SCRIPT = os.path.join(HERE, "transcribe.py")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--compute", default="int8_float16")
    ap.add_argument("--model", default="large-v3")
    ap.add_argument("--batch", type=int, default=0)
    ap.add_argument("--beam", type=int, default=5)
    ap.add_argument("--lang", default=None, help="force a language, e.g. th")
    ap.add_argument("--no-repeat-ngram", type=int, default=0)
    ap.add_argument("--only", default=None, help="comma list e.g. FTC03,FTC04")
    args = ap.parse_args()

    os.makedirs(OUTDIR, exist_ok=True)
    wavs = sorted(glob.glob(os.path.join(AUDIO, "FTC*.wav")))
    if args.only:
        want = {x.strip().upper() for x in args.only.split(",")}
        wavs = [w for w in wavs if os.path.basename(w)[:5].upper() in want]

    jobs = []
    for w in wavs:
        stem = os.path.splitext(os.path.basename(w))[0]
        out = os.path.join(OUTDIR, stem)
        if os.path.exists(out + ".md"):
            print(f"skip {stem} (already done)")
            continue
        cmd = [sys.executable, SCRIPT, w, out, "--model", args.model,
               "--compute", args.compute, "--beam", str(args.beam)]
        if args.batch > 0:
            cmd += ["--batch", str(args.batch)]
        if args.lang:
            cmd += ["--lang", args.lang]
        if args.no_repeat_ngram > 0:
            cmd += ["--no-repeat-ngram", str(args.no_repeat_ngram)]
        jobs.append((stem, cmd))

    if not jobs:
        print("nothing to do")
        return

    print(f"queue: {[j[0] for j in jobs]}  workers={args.workers}  "
          f"compute={args.compute} batch={args.batch}", flush=True)

    running = []
    t0 = time.time()
    while jobs or running:
        while jobs and len(running) < args.workers:
            stem, cmd = jobs.pop(0)
            log = open(os.path.join(OUTDIR, f"{stem}.log"), "w", encoding="utf-8")
            p = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT)
            running.append((stem, p, log, time.time()))
            print(f"[{time.time()-t0:6.0f}s] START {stem}", flush=True)
        time.sleep(2)
        for item in running[:]:
            stem, p, log, started = item
            if p.poll() is not None:
                log.close()
                state = "OK" if p.returncode == 0 else f"FAIL({p.returncode})"
                print(f"[{time.time()-t0:6.0f}s] {state:8} {stem} "
                      f"({time.time()-started:.0f}s)", flush=True)
                running.remove(item)

    print(f"[{time.time()-t0:6.0f}s] all done", flush=True)

if __name__ == "__main__":
    main()
