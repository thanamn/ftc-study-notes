from itertools import product, combinations

print("=== verify both circuits against the 4 spec relationships ===")
relations = [((0,0,1,1),(1,0)), ((0,1,1,0),(0,1)), ((1,1,0,0),(0,1)), ((1,0,0,1),(1,0))]
N = [r[0] for r in relations]

def L(A,B,C,D): return ((A&D)+(C&D), (A&B)+(B&C))                 # left: X=AD+CD, Y=AB+BC
def Rx(A,B,C,D): return ((1-A)*(1-B)*C*D) + (A*(1-B)*(1-C)*D)     # right X = A'B'CD + AB'C'D
def Ry(A,B,C,D): return ((1-A)*B*C*(1-D)) + (A*B*(1-C)*(1-D))     # right Y = A'BCD' + ABC'D'
def R(A,B,C,D): return (Rx(A,B,C,D), Ry(A,B,C,D))

print(" input      spec    left    right   ok?")
for (ab, spec) in relations:
    A,B,C,D = ab
    print("  %s  %s  %s  %s  %s" % (ab, spec, L(A,B,C,D), R(A,B,C,D), L(A,B,C,D)==spec==R(A,B,C,D)))

print("\n=== 5.2 right circuit, fault: C-pin of gate A'B'CD stuck-at-1 ===")
def Rx_f(A,B,C,D): return ((1-A)*(1-B)*1*D) + (A*(1-B)*(1-C)*D)   # gate1 becomes A'B'D
for (ab, spec) in relations:
    A,B,C,D = ab
    print("  %s normal=%s fault=%s %s" % (ab, R(A,B,C,D), (Rx_f(A,B,C,D), Ry(A,B,C,D)),
          "unchanged" if R(A,B,C,D)==(Rx_f(A,B,C,D),Ry(A,B,C,D)) else "CHANGED"))

print("\n=== 5.1 left circuit, fault: A-pin of gate AD stuck-at-0 ===")
def Lx_f(A,B,C,D): return (0) + (C&D)
for (ab, spec) in relations:
    A,B,C,D = ab
    print("  %s normal=%s fault=%s %s" % (ab, L(A,B,C,D), (Lx_f(A,B,C,D), (A&B)+(B&C)),
          "unchanged" if L(A,B,C,D)==(Lx_f(A,B,C,D),(A&B)+(B&C)) else ("NON-CODE" if (Lx_f(A,B,C,D),(A&B)+(B&C))==(0,0) else "WRONG")))

print("\n=== 2.5 check: is S3 the best for all R and widest 1.5x range? ===")
def s0(R): return R*R
def s1(R): return (1-(1-R)**2)*(1-(1-R)**3)
def s2(R): return R*(1-(1-R)**2)**2 + (1-R)*(1-(1-R*R)**2)
def s3(R): return R**2*(1-(1-R)**3)**2 + 2*R*(1-R)*(1-(1-(1-(1-R)**2)**2)*(1-R*R)) + (1-R)**2*(1-(1-R*R)**3)
ok_s3 = all(s3(k/1000) >= s1(k/1000)-1e-9 and s3(k/1000) >= s2(k/1000)-1e-9 for k in range(1,1000))
print("  S3 >= S1 and S3 >= S2 for all R in (0,1):", ok_s3)
