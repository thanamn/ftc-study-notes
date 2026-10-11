# FTC Study Corpus

AI-optimized extraction of the **2110473 Fault Tolerant Computing** lecture slides.

## Why there is no OCR here

The lecture PDFs are **born-digital** (exported from PowerPoint), so the text is
already embedded and perfect. Extracting it is *exact* and *free*. OCR on these
files would only introduce errors. The only scanned material in the course folder
is photos of **your own handwritten exercise answers** — they are your work, not
source material, so they are deliberately excluded.

## Layout

| Path | What it is | Use it for |
|------|------------|-----------|
| `<lecture>.md` | Slide-anchored Markdown (`## Slide N: Title`) | Reading, quoting, citing by slide |
| `<lecture>.jsonl` | One JSON object per slide | Chunking / RAG / programmatic use |
| `ALL_LECTURES.md` | Every slide, concatenated | Whole-course context in one file |
| `images/*.png` | Rendered pages for visual slides | Diagrams, circuits, tables, formulas |
| `manifest.json` | Machine-readable index | Inventory / tooling |

Each `.jsonl` record:

```json
{"lecture": "...", "slide": 5, "title": "...", "text": "...", "visual": true, "image": "images/....png"}
```

## The `visual` flag

A slide is tagged `visual: true` (and gets an `images/*.png`) when plain text is
**not enough**: it is near text-free, dominated by a picture, or dense with
vector drawings (tables, circuits, diagrams). 247 of 454 slides are visual —
this course is diagram-heavy.

## Using it with an AI, cheaply

1. **Text first.** Feed the `.md` / `.jsonl` text — the whole course is only
   ~150k characters (~40k tokens), so it fits in context for very little.
2. **Images only when the text is ambiguous.** Feed the `images/*.png` for
   `visual: true` slides. This is the only part that costs real money, so do it
   selectively rather than all at once.
3. **Cite by slide.** Every extract keeps `Slide N` anchors, so answers stay
   verifiable against the original deck.

## Caveats of text extraction

- Tables flatten into loose values → trust the image for those slides.
- Math loses overbars/superscripts (e.g. `R1R2'B2R3`) → trust the image.
- Figure-only slides yield just a page number → the image is the content.

## Regenerating

```pwsh
python build_corpus.py        # rewrites study_corpus/ from slides/
```
