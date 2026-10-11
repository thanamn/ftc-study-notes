"""
Build an AI-digestible study corpus from the born-digital lecture PDFs.

Outputs (study_corpus/):
  <lecture>.md      -> human/AI-readable, slide-anchored Markdown
  <lecture>.jsonl   -> one JSON record per slide (ideal for chunking / RAG)
  ALL_LECTURES.md   -> everything in one file
  images/*.png      -> rendered pages for figure/formula-only slides
  README.md         -> corpus guide
  manifest.json     -> machine-readable index
"""
import fitz, glob, os, re, json

ROOT = r"C:\Users\thana\Desktop\fault_tolerant_computing"
os.chdir(ROOT)
OUT = os.path.join(ROOT, "study_corpus")
IMG = os.path.join(OUT, "images")
os.makedirs(IMG, exist_ok=True)

FIX = {
    "\ufb01": "fi", "\ufb02": "fl", "\ufb00": "ff", "\ufb03": "ffi", "\ufb04": "ffl",
    "\u2019": "'", "\u2018": "'", "\u201c": '"', "\u201d": '"',
    "\u2013": "-", "\u2014": "-", "\u00a0": " ",
}
def clean(s):
    for a, b in FIX.items():
        s = s.replace(a, b)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()

def page_title(page):
    d = page.get_text("dict")
    best = (0.0, "")
    for b in d["blocks"]:
        if b.get("type") != 0:
            continue
        for l in b["lines"]:
            for s in l["spans"]:
                t = s["text"].strip()
                if len(t) > 1 and s["size"] > best[0]:
                    best = (s["size"], t)
    return best[1]

def visual_required(page):
    """A slide needs its picture for full meaning if it is (near) text-free,
    dominated by a raster image, or dense with vector drawings (tables,
    circuits, diagrams)."""
    if len(page.get_text().strip()) < 60:
        return True
    area = abs(page.rect.width * page.rect.height) or 1
    cov = sum(abs(r.width * r.height)
              for im in page.get_images(full=True)
              for r in page.get_image_rects(im[0])) / area
    if cov > 0.15:
        return True
    if len(page.get_drawings()) > 8:      # tables / circuits / diagrams
        return True
    return False

def build(lecture_filter=None):
    manifest = []
    all_md = ["# 2110473 Fault Tolerant Computing — Full Slide Corpus\n",
              "> Extracted from born-digital lecture PDFs with PyMuPDF (exact text, no OCR).\n",
              "> Every slide is tagged; `visual: true` slides have a rendered "
              "image in `images/` so diagrams and tables stay readable.\n"]

    for f in sorted(glob.glob(os.path.join("materials", "lecture_slides", "*.pdf"))):
        name = os.path.basename(f)
        if lecture_filter and lecture_filter not in name:
            continue
        stem = re.sub(r"^(2110473_2026S1_|2026S1_)", "", name).split("-9294-")[0]
        doc = fitz.open(f)
        nslides = len(doc)

        md = [f"# {stem}\n",
              f"> Source: `{name}` — {nslides} slides. "
              "`visual: true` slides have a rendered image in `images/`.\n"]
        records = []

        for i, page in enumerate(doc, 1):
            raw = clean(page.get_text("text", sort=True))
            title = clean(page_title(page))
            body = raw
            # drop the duplicated title line and a trailing standalone page number
            if title and body.startswith(title):
                body = body[len(title):].strip()
            body = re.sub(rf"\n\s*{i}\s*$", "", body).strip()

            is_visual = visual_required(page)
            img_rel = None
            if is_visual:
                img_rel = f"images/{stem}_s{i:03d}.png"
                pix = page.get_pixmap(dpi=140)
                pix.save(os.path.join(OUT, img_rel))

            heading = f"## Slide {i}" + (f": {title}" if title else "")
            if is_visual:
                heading += "  *(visual)*"

            md.append(heading)
            if body:
                md.append(body)
            if img_rel:
                md.append(f"![{stem} slide {i}]({img_rel})")
            md.append("")

            records.append({
                "lecture": stem, "slide": i, "title": title,
                "text": body, "visual": is_visual, "image": img_rel,
            })

        with open(os.path.join(OUT, f"{stem}.md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(md).rstrip() + "\n")
        with open(os.path.join(OUT, f"{stem}.jsonl"), "w", encoding="utf-8") as fh:
            for r in records:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")

        figs = sum(1 for r in records if r["visual"])
        manifest.append({"file": name, "lecture": stem, "slides": nslides,
                         "visual_slides": figs, "text_only_slides": nslides - figs})
        all_md.append("\n".join(md))
        all_md.append("\n---\n")
        doc.close()
        print(f"{stem:<34} {nslides:>3} slides, {figs:>3} visual")

    with open(os.path.join(OUT, "ALL_LECTURES.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(all_md).rstrip() + "\n")
    with open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)
    return manifest

if __name__ == "__main__":
    m = build()
    print(f"\nTotal: {sum(x['slides'] for x in m)} slides, "
          f"{sum(x['visual_slides'] for x in m)} visual (images rendered), "
          f"{sum(x['text_only_slides'] for x in m)} text-only.")
