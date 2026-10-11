"""Extract text from homework/exercise PDFs for study purposes."""
import os
import glob
import pymupdf

ROOT = r"C:\Users\thana\Desktop\fault_tolerant_computing"
os.chdir(ROOT)

groups = [
    ("homework", glob.glob(os.path.join("materials", "homework", "*.pdf"))),
    ("exercises", glob.glob(os.path.join("materials", "exercises", "*.pdf"))),
]

out = []
for label, files in groups:
    for p in sorted(files):
        if "_duplicates" in p:
            continue
        try:
            d = pymupdf.open(p)
        except Exception as e:
            out.append(f"===== {p} ERROR {e!r} =====")
            continue
        out.append(f"\n===== {p} ({len(d)} pages) =====")
        for i, pg in enumerate(d, 1):
            t = pg.get_text("text").strip()
            out.append(f"----- page {i} textlen={len(t)} -----")
            out.append(t)
        d.close()

text = "\n".join(out)
os.makedirs("study_corpus", exist_ok=True)
with open(os.path.join("study_corpus", "HOMEWORK_EXERCISES_RAW.md"), "w", encoding="utf-8") as fh:
    fh.write(text)
print(f"wrote {len(text)} chars")
