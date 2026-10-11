# 2110473 Fault Tolerant Computing — study workspace

Everything for the course, organised so an AI (or you) can navigate it quickly.

## Layout

```
fault_tolerant_computing/
├── materials/                     # course inputs (never modified)
│   ├── lecture_slides/            # 7 lecture decks + syllabus + weekly plan (PDF)
│   ├── exercises/                 # your completed exercise sheets (scans/PDF)
│   │   └── _duplicates/           # exact duplicate of Circwit.pdf (same MD5)
│   ├── homework/                  # HW#01 … HW06 sheets
│   └── exams/                     # senior exam recollection (.docx + .md + image)
├── study_corpus/                  # generated, AI-ready study material
│   ├── FTC01…FTC07.md             # slide-anchored Markdown (per lecture)
│   ├── FTC01…FTC07.jsonl          # one record per slide (RAG-ready)
│   ├── ALL_LECTURES.md            # every slide in one file
│   ├── images/                    # rendered pages for visual-only slides
│   ├── qa/                        # question banks (active recall)
│   ├── transcripts/               # lecture-clip transcripts — FTC02…FTC07 (Whisper)
│   ├── manifest.json              # machine-readable index
│   └── README.md                  # how the corpus was built + how to use it
├── exam_script/                   # exam-prep notes: course map, topic notes, drills
├── tools/                         # scripts
│   ├── build_corpus.py            # PDF slides -> study_corpus (no OCR needed)
│   ├── extract_docx.py            # .docx -> Markdown (paragraphs + tables)
│   ├── transcribe.py              # Whisper transcription (GPU)
│   ├── run_batch.py               # queue transcription across lectures
│   └── fetch_audio.ps1            # signed Kaltura URL -> 16 kHz mono WAV
└── README.md
```

## Pipeline

1. **Slides** are born-digital → text extracted exactly, free (`tools/build_corpus.py`).
   Figure/table/formula-only slides are rendered as images so nothing is lost.
2. **Lecture clips** live on Kaltura behind the LMS login and have **no captions**,
   so they are transcribed locally with **faster-whisper `large-v3`** on the GPU.
   Audio is pulled via the player's signed HLS URL (`tools/fetch_audio.ps1`).

### Transcription notes
- Config: `large-v3 · float16 · batch 16 · beam 5 · --lang th · --no-repeat-ngram 3`.
  Batching is what makes it fast (~8× realtime); forcing `th` prevents English
  hallucination; `no-repeat-ngram 3` cures repetition loops on rough audio.
- **FTC01 was skipped** — audio too echoey and the content is intro-level, fully
  covered by the slides. See `study_corpus/transcripts/README.md`.

## Regenerating

```pwsh
python tools/build_corpus.py                    # rebuild study_corpus from materials/lecture_slides
python tools/run_batch.py --only FTC05          # (re)transcribe specific lectures
```

Audio working files and Whisper weights live under `%LOCALAPPDATA%\Temp\opencode\`
(`ftc_audio/`, `whisper_models/`) to keep this tree small.
