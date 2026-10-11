import os, pymupdf
ROOT = r"C:\Users\thana\Desktop\fault_tolerant_computing"
os.chdir(ROOT)
d = pymupdf.open("materials/homework/HW02 System Reliability_6a82623d7a643.pdf")
pg = d[0]
# crop region containing the two diagrams (roughly upper-middle of page)
r = pymupdf.Rect(60, 320, 560, 560)
pix = pg.get_pixmap(dpi=300, clip=r)
pix.save("study_corpus/images/probe_hw02_zoom.png")
print("ok", pix.width, pix.height)
