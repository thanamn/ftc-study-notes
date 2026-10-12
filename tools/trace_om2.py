import sys

def majority(vals):
    a=vals.count('A'); r=vals.count('R')
    if a>r: return 'A'
    if r>a: return 'R'
    return 'R'          # Lamport: tie -> RETREAT

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

def show(title, adv):
    nodes=[1,2,3,4,5,6]; faulty={2,3}
    dec,recv,sub=om(2,1,[2,3,4,5,6],faulty,adv,'A')
    print("== %s =="%title)
    print("  loyal decisions:", {("N%d"%k):dec[k] for k in [4,5,6]})
    for i in [4,5,6]:
        row=[("N%d"%j, sub[j][i]) for j in [2,3,4,5,6] if j!=i]
        print("    N%d: C=%s | %s => majority=%s"%(i, recv[i], ", ".join("%s=%s"%r for r in row), dec[i]))
    print()

# 1) faulty always send R (per problem statement)
advR={}
for c in [2,3]:
    for t in [1,2,3,4,5,6]:
        if t!=c: advR[(c,t)]='R'
show("faulty N2,N3 always send R", advR)

# 2) faulty adversarial (can send different msgs) - search one giving disagreement
from itertools import product
pairs=[(c,t) for c in [2,3] for t in [1,2,3,4,5,6] if t!=c]
found=None
for bits in product('AR',repeat=len(pairs)):
    adv={p:v for p,v in zip(pairs,bits)}
    dec,recv,sub=om(2,1,[2,3,4,5,6],{2,3},adv,'A')
    if len({dec[4],dec[5],dec[6]})>1:
        found=(adv,dec,recv,sub); break
if found:
    adv,dec,recv,sub=found
    print("== adversarial faulty (different msgs) -> loyal DISAGREE ==")
    print("  adversary N2->:", {("N%d"%t):adv[(2,t)] for t in [3,4,5,6]})
    print("  adversary N3->:", {("N%d"%t):adv[(3,t)] for t in [2,4,5,6]})
    print("  loyal decisions:", {("N%d"%k):dec[k] for k in [4,5,6]})
    for i in [4,5,6]:
        row=[("N%d"%j, sub[j][i]) for j in [2,3,4,5,6] if j!=i]
        print("    N%d: C=%s | %s => majority=%s"%(i, recv[i], ", ".join("%s=%s"%r for r in row), dec[i]))
