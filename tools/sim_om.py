from itertools import product

def majority(vals):
    a = vals.count('A'); r = vals.count('R')
    if a > r: return 'A'
    if r > a: return 'R'
    return 'TIE'

def om(m, c, L, faulty, adv, cval):
    # returns dict l -> decided value for l in L (meaningful for loyal l)
    recv = {}
    for l in L:
        recv[l] = adv[(c, l)] if c in faulty else cval
    if m == 0:
        return dict(recv)
    sub = {}
    for i in L:
        others = [x for x in L if x != i]
        val_i = adv[(i, others[0])] if i in faulty else recv[i]
        sub[i] = om(m - 1, i, others, faulty, adv, val_i)
    dec = {}
    for i in L:
        # include the value i itself received from the commander, plus relays from others
        vals = [recv[i]] + [sub[j][i] for j in L if j != i]
        dec[i] = majority(vals)
    return dec

def run(nodes, faulty, adv, m, commander=1, cval='A'):
    L = [x for x in nodes if x != commander]
    dec = om(m, commander, L, set(faulty), adv, cval)
    return {i: dec[i] for i in L if i not in faulty}

def search_failure(nodes, faulty, m, cval='A'):
    # brute force adversary over (faulty, target) pairs with values A/R
    targets = nodes
    pairs = [(c, t) for c in faulty for t in targets if t != c]
    found = None
    for bits in product('AR', repeat=len(pairs)):
        adv = {p: v for p, v in zip(pairs, bits)}
        for (c, t) in product(faulty, nodes):
            adv.setdefault((c, t), 'R')
        dec = run(nodes, faulty, adv, m, cval=cval)
        vals = set(dec.values())
        if len(vals) > 1:
            found = (adv, dec)
            break
        if 'TIE' in vals:
            found = (adv, dec)
            break
    return found

print("=== Check n=4, m=1 (should always agree) ===")
f = search_failure([1,2,3,4], [4], 1)
print("  found disagreement?", f is not None, f[1] if f else "")

print()
print("=== Check n=6, m=2, faulty {2,3} (should FAIL) ===")
f = search_failure([1,2,3,4,5,6], [2,3], 2)
print("  found disagreement?", f is not None)
if f:
    adv, dec = f
    print("  loyal decisions:", dec)

print()
print("=== n=6,m=2 with faulty STRICTLY sending R only ===")
adv = {}
for c in (2,3):
    for t in range(1,7):
        if t != c: adv[(c,t)] = 'R'
dec = run([1,2,3,4,5,6], [2,3], adv, 2)
print("  loyal decisions:", dec)

print()
print("=== Also: n=7, m=2 (should agree) ===")
f = search_failure([1,2,3,4,5,6,7], [2,3], 2)
print("  found disagreement?", f is not None, (f[1] if f else ""))
