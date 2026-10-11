# A/B report — choosing the transcription config (FTC03 slice)

Test audio: **FTC03, 150 s slice starting at 15:00** (clean lecture).
Machine: RTX 4060 Laptop (8 GB), faster-whisper, `ffmpeg`.

## The real problem was batching, not the model

The first run used the default `beam_size=5` **without** batched inference and
crawled at **~0.4× realtime** (a 75-min lecture ≈ 3 h). The GPU sat at *100%
util but only 25 W* — it was idling between decode steps, waiting on Python.
Enabling **batched inference** fixed it: **0.4× → ~8.5×** (≈20× faster).

## Warm results (models cached; includes ~6 s load)

| Config | Time (150 s slice) | Rate |
|---|---|---|
| `large-v3-turbo` · batch16 · beam5 | 10.2 s | 14.7× |
| `large-v3-turbo` · batch16 · beam1 | 8.9 s | 16.9× |
| `large-v3` · batch16 · beam5 · **float16** | 17.8 s | **8.4×** |
| `large-v3` · batch16 · beam5 · int8_float16 | 23.7 s | 6.3× |
| `large-v3` · batch16 · beam1 | 15.4 s | 9.7× |

Notes:
- First turbo call also paid a one-time ~1.6 GB model download.
- `int8_float16` was **slower** here — the 4060's int8 path doesn't pay off for this model.

## Why turbo was rejected — Thai quality

Same slice, same segment:

- **large-v3:** `...เรียกว่า K-Fault Tolerance นั่นเอง... Process ... Error Correction ... 2K บวก 1 ... Detect ... Correct ...`
- **turbo:** `...k-fault ทอร์แรง... โปรเศษย์... Error Collection... Correx... ผิดภาท...`

Turbo mangles Thai words and technical English terms; **large-v3 is clearly
more accurate**. Since the lectures are Thai (and FTC01/02 are echoey), accuracy
beats the 1.7× speed gain.

## VRAM

One batched `large-v3` worker (float16, batch16) = **7941 MiB / 8188 MiB at 100% util**.
Batching already saturates the GPU, so extra parallel workers add nothing and OOM.

## Decision

```
large-v3 · float16 · batch 16 · beam 5 · 1 worker
=> ~8.4× realtime, ~60 min for all 7 lectures (was ~10 h)
```
