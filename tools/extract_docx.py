"""
Extract a .docx to Markdown, preserving paragraph/table order.

    python extract_docx.py <input.docx> <output.md>
"""
import sys
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn


def iter_block_items(parent):
    body = parent.element.body
    for child in body.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, parent)
        elif child.tag == qn("w:tbl"):
            yield Table(child, parent)


def table_to_md(tbl):
    rows = []
    for r in tbl.rows:
        cells = [c.text.strip().replace("\n", " ") for c in r.cells]
        rows.append(cells)
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |",
           "| " + " | ".join(["---"] * width) + " |"]
    for r in rows[1:]:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)


def main():
    src, dst = sys.argv[1], sys.argv[2]
    doc = Document(src)
    lines = []
    for block in iter_block_items(doc):
        if isinstance(block, Paragraph):
            t = block.text.strip()
            if not t:
                continue
            style = (block.style.name or "").lower()
            if style.startswith("heading"):
                lines.append("## " + t)
            else:
                lines.append(t)
        else:
            lines.append("")
            lines.append(table_to_md(block))
            lines.append("")
    text = "\n\n".join(lines).strip() + "\n"
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {dst}: {len(text)} chars, {text.count(chr(10))+1} lines")


if __name__ == "__main__":
    main()
