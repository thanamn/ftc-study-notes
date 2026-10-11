import os
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

os.chdir(r"C:\Users\thana\Desktop\fault_tolerant_computing")
doc = Document("materials/exams/Fault Tolerant (senior exam).docx")

def iter_blocks(parent):
    for child in parent.element.body.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, parent)
        elif child.tag == qn("w:tbl"):
            yield Table(child, parent)

out = []
for b in iter_blocks(doc):
    if isinstance(b, Paragraph):
        t = b.text.strip()
        if t:
            out.append("P: " + t)
    else:
        out.append("TABLE:")
        for r in b.rows:
            out.append("  | " + " | ".join(c.text.strip().replace(chr(10), " ") for c in r.cells))

with open("study_corpus/SENIOR_EXAM_docx.md", "w", encoding="utf-8") as fh:
    fh.write("\n".join(out))
print("wrote", len(out), "blocks")
