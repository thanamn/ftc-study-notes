# Systematic cyclic encoding over GF(2)
# Convention (course HW05): data bit b_i (leftmost = i=0) is coefficient of x^i.
# g(x) = x^4 + x^3 + x^2 + x + 1  -> coefficients [g0..g4] = [1,1,1,1,1]

def polymod(a, b):
    # a, b as ints (bit i = coeff of x^i); return a mod b over GF(2)
    db = b.bit_length()
    while a.bit_length() >= db:
        a ^= b << (a.bit_length() - db)
    return a

def bits_to_int(bits):
    # bits: string, leftmost = x^0
    v = 0
    for i, ch in enumerate(bits):
        if ch == '1':
            v |= (1 << i)
    return v

def int_to_bits(v, length):
    return ''.join('1' if (v >> i) & 1 else '0' for i in range(length))

def encode_systematic(data_str, g_int, r):
    m = bits_to_int(data_str)
    shifted = m << r
    rem = polymod(shifted, g_int)
    cw = (m << r) | rem
    return int_to_bits(cw, len(data_str) + r), int_to_bits(rem, r)

g = 0b11111  # x^4+x^3+x^2+x+1
r = 4
print("g(x) = x^4+x^3+x^2+x+1 = 11111, r = 4, n = 10, k = 6")
for d in ["011000", "010101", "111111", "100100", "001100"]:
    cw, rem = encode_systematic(d, g, r)
    print("  data=%s  remainder=%s  codeword=%s" % (d, rem, cw))

# Also non-systematic: data * g
def encode_nonsep(data_str, g_int):
    m = bits_to_int(data_str)
    prod = 0
    gg = g_int
    v = m
    i = 0
    while v:
        if v & 1:
            prod ^= gg << i
        v >>= 1
        i += 1
    return int_to_bits(prod, 10)

print()
print("non-systematic (data * g):")
for d in ["011000", "010101"]:
    print("  data=%s  codeword=%s" % (d, encode_nonsep(d, g)))
