from itertools import combinations

# Code A = rows 1-7 (row 7 typed as '1110111' -> take 6 bits '111011', flag it)
rows = ["001100", "011100", "011110", "010010", "011111", "110011"]
row7 = "111011"          # from '1110111' (dropped the trailing bit)
C = rows + [row7]
print("Code A =", C)

def hd(a, b): return sum(x != y for x, y in zip(a, b))

print("\n=== 4.1  pairwise Hamming distances ===")
mn = 99
for i, j in combinations(range(len(C)), 2):
    d = hd(C[i], C[j])
    mn = min(mn, d)
    print("  d(%s,%s)=%d" % (C[i], C[j], d))
print("=> n=%d, M=%d, d=%d  =>  notation (%d,%d,%d)" % (len(C[0]), len(C), mn, len(C[0]), len(C), mn))

print("\n=== 4.2  candidate row 8 (distinct, keeps min-distance) ===")
best = []
for k in range(64):
    w = format(k, '06b')
    if w in C: continue
    md = min(hd(w, c) for c in C)
    best.append((md, w))
best.sort(reverse=True)
print("  row 8 that maximizes min-distance:", best[0])
print("  (any word not duplicated keeps d; e.g.", best[0][1], "or", best[1][1], ")")

print("\n=== 4.3  Berger code (choose 001100) ===")
w = "001100"; k = len(w)
c = 0
while (1 << c) < k + 1: c += 1
ones = w.count('1')
cnt = format(ones, '0%db' % c)
comp = ''.join('1' if ch == '0' else '0' for ch in cnt)
print("  k=%d -> c=%d ; #1=%d -> %s -> complement %s -> Berger = %s %s" % (k, c, ones, cnt, comp, w, comp))

print("\n=== 4.4  Cyclic (10,6), g = x^4+x^3+x^2+x+1 = 11111 ===")
g = 0b11111; r = 4
def gf2_mod(a, g):
    db = g.bit_length()
    while a.bit_length() >= db:
        a ^= g << (a.bit_length() - db)
    return a
data = "001100"
shifted = int(data + "0"*r, 2)          # data shifted left by r
rem = gf2_mod(shifted, g)
codeword = data + format(rem, '0%db' % r)
print("  systematic : data %s -> remainder %s -> codeword %s  (check mod=%d)"
      % (data, format(rem, '0%db' % r), codeword, gf2_mod(int(codeword, 2), g)))
# non-separable multiply: data*g
prod = 0; x = int(data, 2); i = 0
while x:
    if x & 1: prod ^= g << i
    x >>= 1; i += 1
print("  multiply   : data %s x g = %s" % (data, format(prod, '010b')))
