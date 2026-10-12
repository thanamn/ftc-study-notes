from itertools import combinations

print("=== Q5a: x=ad+cd, y=ab+bc, a stuck at 0 ===")
ins = [(0, 0, 1, 1), (0, 1, 1, 0), (1, 1, 0, 0), (1, 0, 0, 1)]
def xf(a, b, c, d): return a * d + c * d
def yf(a, b, c, d): return a * b + b * c
def cw(xv, yv): return (xv, yv) in [(1, 0), (0, 1)]
for (a, b, c, d) in ins:
    xv, yv = xf(a, b, c, d), yf(a, b, c, d)
    xg, yg = xf(0, b, c, d), yf(0, b, c, d)
    print("  (a,b,c,d)=%s normal=(%d,%d) cw=%s | a-sa0=(%d,%d) cw=%s"
          % ((a, b, c, d), xv, yv, cw(xv, yv), xg, yg, cw(xg, yg)))

print()
print("=== Q5b: x=A'B'CD+AB'C'D, y=A'BCD'+ABC'D', C stuck at 1 ===")
def x2(A, B, C, D):
    return ((1 - A) & (1 - B) & C & D) + (A & (1 - B) & (1 - C) & D)
def y2(A, B, C, D):
    return ((1 - A) & B & C & (1 - D)) + (A & B & (1 - C) & (1 - D))
for A in (0, 1):
    for B in (0, 1):
        for C in (0, 1):
            for D in (0, 1):
                xv, yv = x2(A, B, C, D), y2(A, B, C, D)
                if (xv, yv) in [(1, 0), (0, 1)]:
                    g, h = x2(A, B, 1, D), y2(A, B, 1, D)
                    print("  (%d,%d,%d,%d) cw=(%d,%d) | C-sa1=(%d,%d) cw=%s"
                          % (A, B, C, D, xv, yv, g, h, (g, h) in [(1, 0), (0, 1)]))

print()
print("=== Q6: code A pairwise distances ===")
C = ["1111111", "1111011", "0000111", "1101111", "0011000", "0110000"]
def hd(u, v): return sum(a != b for a, b in zip(u, v))
mn = 99
for i, j in combinations(range(len(C)), 2):
    d = hd(C[i], C[j])
    mn = min(mn, d)
    print("  d(%s,%s)=%d" % (C[i], C[j], d))
print("  min distance =", mn, " length=", len(C[0]), " M=", len(C))
C6 = [w[:6] for w in C]
mn6 = min(hd(C6[i], C6[j]) for i, j in combinations(range(len(C6)), 2))
print("  shortened to 6 bits:", C6, "min distance=", mn6)

print()
print("=== Q2 polynomials & inequality ===")
def R21(R): return R * R
def R22(R): return 1 - (1 - R * R) ** 2
def R23(R): return R * (2 * R - R * R) ** 2 + (1 - R) * (1 - (1 - R * R) ** 2)
for R in [0.5, 0.7, 0.8, 0.9, 0.95]:
    print("  R=%.2f: 2.1=%.4f 2.2=%.4f 2.3=%.4f  1.2*2.1=%.4f"
          % (R, R21(R), R22(R), R23(R), 1.2 * R21(R)))
def root(f):
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if f(mid) > 0: lo = mid
        else: hi = mid
    return lo
print("  2.2 > 1.2*2.1 for R <", round(root(lambda r: R22(r) - 1.2 * R21(r)), 4))
print("  2.3 > 1.2*2.1 for R <", round(root(lambda r: R23(r) - 1.2 * R21(r)), 4))
print("  2.3 >= 2.2 for all R in [0,1]:",
      all(R23(k / 100.0) >= R22(k / 100.0) - 1e-12 for k in range(101)))
print("  2.2 >= 2.1 for all R in [0,1]:",
      all(R22(k / 100.0) >= R21(k / 100.0) - 1e-12 for k in range(101)))
s = "2R^2+2R^3-5R^4+2R^5"
print("  expanded 2.3 =", s, "(check R=1 ->", R23(1.0), ")")
