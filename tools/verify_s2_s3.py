def reliability(edges, probs):
    comps = list(edges.items())  # ((u,v), name)
    n = len(comps)
    total = 0.0
    for mask in range(2 ** n):
        parent = {}
        def find(a):
            parent.setdefault(a, a)
            r = a
            while parent[r] != r: r = parent[r]
            while parent[a] != r: parent[a], a = r, parent[a]
            return r
        p = 1.0
        for i, ((u, v), name) in enumerate(comps):
            if mask >> i & 1:
                p *= probs[name]
                parent[find(u)] = find(v)
            else:
                p *= (1 - probs[name])
        if find(0) == find('Y'):
            total += p
    return total

S2 = dict([((0,1),'A1'),((0,2),'A2'),((1,'Y'),'B1'),((2,'Y'),'B2'),((1,2),'K')])
S3 = dict([((0,1),'A1'),((0,2),'A2'),((0,3),'A3'),
           ((1,'Y'),'B1'),((2,'Y'),'B2'),((3,'Y'),'B3'),
           ((1,2),'K1'),((2,3),'K2')])

def S1_formula(Ra, Rb, Rk): return (1-(1-Ra)**2)*(1-(1-Rb)**3)
def S2_formula(Ra, Rb, Rk):
    return Rk*(1-(1-Ra)**2)*(1-(1-Rb)**2) + (1-Rk)*(1-(1-Ra*Rb)**2)
def S3_formula(Ra, Rb, Rk):
    P12 = (1-(1-Ra)**2)*(1-(1-Rb)**2)      # merged pair works
    Pone = Ra*Rb
    return (Rk**2)*(1-(1-Ra)**3)*(1-(1-Rb)**3) \
         + 2*Rk*(1-Rk)*(1-(1-P12)*(1-Pone)) \
         + ((1-Rk)**2)*(1-(1-Ra*Rb)**3)

tests = [(0.9,0.8,0.95),(0.7,0.9,0.6),(0.5,0.99,0.8),(0.85,0.6,0.7)]
for Ra,Rb,Rk in tests:
    pr = {'A1':Ra,'A2':Ra,'A3':Ra,'B1':Rb,'B2':Rb,'B3':Rb,'K':Rk,'K1':Rk,'K2':Rk}
    e2 = reliability(S2, pr); f2 = S2_formula(Ra,Rb,Rk)
    e3 = reliability(S3, pr); f3 = S3_formula(Ra,Rb,Rk)
    print(f"Ra={Ra} Rb={Rb} Rk={Rk} | S2 enum={e2:.6f} formula={f2:.6f} ok={abs(e2-f2)<1e-9} | S3 enum={e3:.6f} formula={f3:.6f} ok={abs(e3-f3)<1e-9}")
