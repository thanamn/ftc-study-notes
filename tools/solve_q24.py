import numpy as np

def mul(p, q):
    r = [0.0]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] += a*b
    return r
def add(p, q):
    n = max(len(p), len(q)); r = [0.0]*n
    for i, a in enumerate(p): r[i] += a
    for i, b in enumerate(q): r[i] += b
    return r
def shift(p, k): return [0.0]*k + p
def scal(p, c): return [c*x for x in p]

# with Ra=Rb=Rk=R:
a = [0, 3, -3, 1]                       # 1-(1-R)^3
a2 = mul(a, a)
t1 = shift(mul(a2, [1.0]), 2)           # R^2 * a^2

u2 = mul([0, 2, -1], [0, 2, -1])        # (2R-R^2)^2
one_minus_u2 = add([1.0], scal(u2, -1.0))
prod = mul(one_minus_u2, [1.0, 0, -1])  # (1-(2R-R^2)^2)(1-R^2)
b = add([1.0], scal(prod, -1.0))        # b = 1 - prod
t2 = scal(mul(mul([0, 1.0], [1.0, -1.0]), b), 2.0)   # 2 R(1-R) b

c = [0, 0, 3, 0, -3, 0, 1]              # 1-(1-R^2)^3
t3 = mul(mul([1.0, -1.0], [1.0, -1.0]), c)           # (1-R)^2 c

Rs3 = add(add(t1, t2), t3)
Rs3 = [round(x, 9) for x in Rs3]
print("Rs3(R) coeffs (R^0..R^8):", Rs3)
print("degree:", len(Rs3)-1)

g = Rs3[:]; g[2] -= 1.5
roots = np.roots(list(reversed(g)))
real = sorted(float(r.real) for r in roots if abs(r.imag) < 1e-9 and 0 < r.real < 1)
print("roots of (Rs3 - 1.5R^2) in (0,1):", [round(x, 6) for x in real])
print("=> Rs3 > 1.5 Rs0 for R <", round(real[0], 4))
for r in [0.7, 0.8, 0.805, 0.809, 0.81, 0.85]:
    val = sum(c0*r**i for i, c0 in enumerate(Rs3))
    print("R=%.3f Rs3=%.6f  Rs3-1.5R^2=%.6f" % (r, val, val-1.5*r*r))
