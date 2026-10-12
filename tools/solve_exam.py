def make_find(parent):
    def find(a):
        parent.setdefault(a, a)
        r = a
        while parent[r] != r:
            r = parent[r]
        while parent[a] != r:
            parent[a], a = r, parent[a]
        return r
    return find

def reliability(edges, R, X=0, Y='Y'):
    """edges: dict {(u,v): name}. Enumerate all working subsets."""
    comps = list(edges.keys())
    n = len(comps)
    total = 0.0
    for mask in range(2 ** n):
        parent = {}
        find = make_find(parent)
        p = 1.0
        for i, c in enumerate(comps):
            if mask >> i & 1:
                p *= R
                parent[find(c[0])] = find(c[1])
            else:
                p *= (1 - R)
        if find(X) == find(Y):
            total += p
    return total

S2 = dict([((0,1),'A1'), ((0,2),'A2'), ((1,'Y'),'B1'), ((2,'Y'),'B2'), ((1,2),'K')])
S3 = dict([((0,1),'A1'), ((0,2),'A2'), ((0,3),'A3'),
           ((1,'Y'),'B1'), ((2,'Y'),'B2'), ((3,'Y'),'B3'),
           ((1,2),'K1'), ((2,3),'K2')])

R_S0 = lambda R: R*R
R_S1 = lambda R: (1-(1-R)**2)*(1-(1-R)**3)
R_S2 = lambda R: reliability(S2, R)
R_S3 = lambda R: reliability(S3, R)

print("Q2: reliability of each scheme (S0 series; S1 2xA-parallel then 3xB-parallel)")
for R in [0.5, 0.7, 0.8, 0.9, 0.95]:
    print("  R=%.2f  S0=%.5f  S1=%.5f  S2=%.5f  S3=%.5f"
          % (R, R_S0(R), R_S1(R), R_S2(R), R_S3(R)))

def thresh(f, k=1.5):
    def g(r): return f(r) - k*R_S0(r)
    if g(1e-6) <= 0: return None
    a, b = 0.0, 1.0
    for _ in range(90):
        m = (a+b)/2
        if g(m) > 0: a = m
        else: b = m
    return a

print()
print("Q2.2  S1 > 1.5*S0  ->  R <", round(thresh(R_S1), 4))
print("Q2.3  S2 > 1.5*S0  ->  R <", round(thresh(R_S2), 4))
print("Q2.4  S3 > 1.5*S0  ->  R <", round(thresh(R_S3), 4))
print()
# compare schemes to each other
print("S2 >= S1 always?", all(R_S2(k/100) >= R_S1(k/100)-1e-12 for k in range(101)))
print("S3 >= S2 always?", all(R_S3(k/100) >= R_S2(k/100)-1e-12 for k in range(101)))
