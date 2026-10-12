from itertools import product

def majority(vals):
    a=vals.count('A'); r=vals.count('R')
    if a>r: return 'A'
    if r>a: return 'R'
    return 'TIE'

def om(m, c, L, faulty, adv, cval):
    recv={l:(adv[(c,l)] if c in faulty else cval) for l in L}
    if m==0:
        return recv, recv, {}
    sub={}
    for i in L:
        others=[x for x in L if x!=i]
        vi=adv[(i,others[0])] if i in faulty else recv[i]
        sub[i]=om(m-1,i,others,faulty,adv,vi)[0]
    dec={}
    for i in L:
        vals=[recv[i]]+[sub[j][i] for j in L if j!=i]
        dec[i]=majority(vals)
    return dec, recv, sub

def run(nodes,faulty,m,adv):
    L=[x for x in nodes if x!=1]
    return om(m,1,L,set(faulty),adv,'A')

# search adversary (faulty nodes 2,3) that makes loyal lieutenants disagree
nodes=[1,2,3,4,5,6]; faulty=[2,3]; m=2
pairs=[(c,t) for c in faulty for t in nodes if t!=c]
found=None
for bits in product('AR',repeat=len(pairs)):
    adv={p:v for p,v in zip(pairs,bits)}
    for (c,t) in product(faulty,nodes):
        adv.setdefault((c,t),'R')
    dec,recv,sub=run(nodes,faulty,m,adv)
    vals=[dec[i] for i in [4,5,6]]
    if len(set(vals))>1:
        found=(adv,dec,recv,sub); break

adv,dec,recv,sub=found
print("adversary (faulty, target) -> msg:")
for k in sorted(adv): print("   N%d -> N%d : %s"%(k[0],k[1],adv[k]))
print("\nOM(2): N1 (loyal) sends A to N2..N6")
print("OM(1): each lieutenant acts as commander; OM(0): relay")
print("\nFinal decisions of loyal lieutenants:", {"N4":dec[4],"N5":dec[5],"N6":dec[6]})
print("\n--- top-level vectors (what each loyal lieutenant collects in step 3) ---")
for i in [4,5,6]:
    row=[("N1",recv[i])]+[("N%d"%j,sub[j][i]) for j in [2,3,4,5,6] if j!=i]
    print("  N%d: "%i + ", ".join("%s=%s"%r for r in row) + "  => majority = %s"%dec[i])
