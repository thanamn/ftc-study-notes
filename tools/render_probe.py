"""Render first page of selected PDFs to PNG for visual inspection."""
import os
import pymupdf

ROOT = r"C:\Users\thana\Desktop\fault_tolerant_computing"
os.chdir(ROOT)
OUT = os.path.join("study_corpus", "images")
os.makedirs(OUT, exist_ok=True)

targets = {
    "hw02": "materials/homework/HW02 System Reliability_6a82623d7a643.pdf",
    "hw04": "materials/homework/HW04 Checkpointing_6a94cea786cc7.pdf",
    "hw06": "materials/homework/HW06 Self-Checking Circuits_6aa745669a26a.pdf",
    "circwit": "materials/exercises/Circwit.pdf",
    "ex_selfcheck": "materials/exercises/Exercise-Self-Checking-Circmit.pdf",
    "ex_cyclic": "materials/exercises/Exercise-Cyclic-Code.pdf",
    "ex_ckt": "materials/exercises/Exercise-Checkpointing.pdf",
    "ex_bft": "materials/exercises/Exercise-Byzantine-Fault-Tolerance.pdf",
}
for key, p in targets.items():
    d = pymupdf.open(p)
    for i, pg in enumerate(d, 1):
        pix = pg.get_pixmap(dpi=130)
        fn = os.path.join(OUT, f"probe_{key}_p{i}.png")
        pix.save(fn)
        print(fn)
    d.close()
