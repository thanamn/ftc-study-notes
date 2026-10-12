from itertools import product

def cw(xv, yv): return (xv, yv) in [(1, 0), (0, 1)]

print("=== Q5.1 LEFT: x = AD + CD, y = AB + BC ; fault: A-pin of gate AD stuck-at-0 ===")
def xl(A, B, C, D): return (A & D) + (C & D)
def yl(A, B, C, D): return (A & B) + (B & C)
def xl_f(A, B, C, D): return 0 + (C & D)          # gate AD forced to 0
print("A B C D | normal(x,y) cw | fault(x,y) cw | normal-codeword?")
for A, B, C, D in product([0, 1], repeat=4):
    xv, yv = xl(A, B, C, D), yl(A, B, C, D)
    xf, yf = xl_f(A, B, C, D), yl(A, B, C, D)
    if cw(xv, yv):   # only input codewords matter
        print(" %d %d %d %d |  (%d,%d)  %s |  (%d,%d)  %s | %s"
              % (A, B, C, D, xv, yv, cw(xv, yv), xf, yf, cw(xf, yf),
                 "still correct" if (xf, yf) == (xv, yv) else ("NON-CODE (detected)" if not cw(xf, yf) else "WRONG CODEWORD")))

print()
print("=== Q5.2 RIGHT: x = A'B'CD + A'BC'D, y = A'BCD' + AB'C'D' ; fault: C-pin of gate A'B'CD stuck-at-1 ===")
def xr(A, B, C, D): return ((1-A) & (1-B) & C & D) + ((1-A) & B & (1-C) & D)
def yr(A, B, C, D): return ((1-A) & B & C & (1-D)) + (A & (1-B) & (1-C) & (1-D))
def xr_f(A, B, C, D): return ((1-A) & (1-B) & 1 & D) + ((1-A) & B & (1-C) & D)  # C pin ->1
print("A B C D | normal(x,y) cw | fault(x,y) cw | normal-codeword?")
for A, B, C, D in product([0, 1], repeat=4):
    xv, yv = xr(A, B, C, D), yr(A, B, C, D)
    xf, yf = xr_f(A, B, C, D), yr(A, B, C, D)
    if cw(xv, yv):
        print(" %d %d %d %d |  (%d,%d)  %s |  (%d,%d)  %s | %s"
              % (A, B, C, D, xv, yv, cw(xv, yv), xf, yf, cw(xf, yf),
                 "still correct" if (xf, yf) == (xv, yv) else ("NON-CODE (detected)" if not cw(xf, yf) else "WRONG CODEWORD")))
