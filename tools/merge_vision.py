"""Merge born-digital slide text with vision descriptions of visual slides."""
import os
import re
import glob

ROOT = r"C:\Users\thana\Desktop\fault_tolerant_computing"
os.chdir(ROOT)
VN = os.path.join("study_corpus", "visual_notes")
OUT = os.path.join("study_corpus", "enriched")
os.makedirs(OUT, exist_ok=True)

# deck base name -> list of vision-note files
MAP = {
    "FTC01_Dependable_Computing": ["FTC01_visual.md"],
    "FTC02_Fault_Tolerant_Systems": ["FTC02_visual.md"],
    "FTC03_Byzantine_Fault_Tolerance": ["FTC03_visual.md"],
    "FTC04_Rollback_Recovery": ["FTC04_visual.md"],
    "FTC05_Coding_Theory": ["FTC05_visual.md"],
    "FTC06_Self_Checking": ["FTC06_visual_A.md", "FTC06_visual_B.md"],
    "FTC07_Fault_Masking": ["FTC07_visual_A.md", "FTC07_visual_B.md"],
    "SYLLABUS_2110473": ["MISC_visual.md"],
    "FTC_Weekly_plan": ["MISC_visual.md"],
}


def parse_vision(path):
    """Return {slide_no: text} from a vision-notes markdown file."""
    if not os.path.exists(path):
        return {}
    txt = open(path, encoding="utf-8").read()
    parts = re.split(r"^## Slide\s+(\d+)\s*$", txt, flags=re.M)
    # parts = [preamble, num, body, num, body, ...]
    out = {}
    for i in range(1, len(parts) - 1, 2):
        n = int(parts[i])
        body = parts[i + 1].strip()
        body = re.sub(r"\n{3,}", "\n\n", body)
        out[n] = body
    return out


def build(deck):
    src = os.path.join("study_corpus", f"{deck}.md")
    if not os.path.exists(src):
        return None
    raw = open(src, encoding="utf-8").read()

    vision = {}
    for vf in MAP.get(deck, []):
        vision.update(parse_vision(os.path.join(VN, vf)))

    # split into slides on lines starting with '## Slide '
    chunks = re.split(r"(?m)^(?=## Slide )", raw)
    header = chunks[0].rstrip()  # file title + source line
    body_slides = chunks[1:]

    lines = [f"# {deck} — Enriched (slide text + vision of visual slides)", ""]
    lines.append("> Text = exact extraction from the born-digital PDF. "
                 "For `visual` slides, a faithful description of the figure/table/formula is added "
                 "under **รายละเอียดจากภาพ**. Vision descriptions are model-produced and marked as such.")
    lines.append("")

    for blk in body_slides:
        m = re.match(r"## Slide\s+(\d+)", blk)
        if not m:
            continue
        n = int(m.group(1))
        # drop the image markdown link line (replaced by the vision description)
        blk = re.sub(r"(?m)^!\[[^\]]*\]\([^)]*\)\s*$", "", blk).rstrip()
        lines.append(blk)
        if n in vision:
            lines.append("")
            lines.append("**รายละเอียดจากภาพ (vision):**")
            lines.append("")
            lines.append(vision[n])
        lines.append("")
        lines.append("---")
        lines.append("")

    out = "\n".join(lines).rstrip() + "\n"
    dst = os.path.join(OUT, f"{deck}_enriched.md")
    open(dst, "w", encoding="utf-8").write(out)
    return deck, n if body_slides else 0, len(vision), len(out)


if __name__ == "__main__":
    for deck in MAP:
        r = build(deck)
        if r:
            print(f"{r[0]:<34} slides={r[1]:>3}  vision_used={r[2]:>3}  chars={r[3]}")
