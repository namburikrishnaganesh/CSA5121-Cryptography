# S-DES constants
IP = [1, 5, 2, 0, 3, 7, 4, 6]
IP_INV = [3, 0, 2, 4, 6, 1, 7, 5]
EP = [3, 0, 1, 2, 1, 2, 3, 0]
P4 = [1, 3, 2, 0]
P10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
P8 = [5, 2, 6, 3, 7, 4, 9, 8]
S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]
S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

def permute(val, table, n_bits=8):
    out = 0
    for t in table:
        out <<= 1
        out |= (val >> (n_bits - 1 - t)) & 1
    return out

def left_shift_5(val, shifts):
    return ((val << shifts) | (val >> (5 - shifts))) & 0x1F

def key_gen(key):
    perm = 0
    for i in range(10):
        perm <<= 1
        perm |= (key >> (9 - P10[i])) & 1
    left = (perm >> 5) & 0x1F
    right = perm & 0x1F
    # K1
    left1 = left_shift_5(left, 1)
    right1 = left_shift_5(right, 1)
    merged1 = (left1 << 5) | right1
    k1 = 0
    for i in range(8):
        k1 <<= 1
        k1 |= (merged1 >> (9 - P8[i])) & 1
    # K2
    left2 = left_shift_5(left1, 2)
    right2 = left_shift_5(right1, 2)
    merged2 = (left2 << 5) | right2
    k2 = 0
    for i in range(8):
        k2 <<= 1
        k2 |= (merged2 >> (9 - P8[i])) & 1
    return k1, k2

def sbox(val, box):
    row = ((val & 0x8) >> 2) | (val & 0x1)
    col = (val >> 1) & 0x3
    return box[row][col]

def f(r, sk):
    ep = 0
    for i in range(8):
        ep <<= 1
        ep |= (r >> (3 - EP[i])) & 1
    x = ep ^ sk
    left = (x >> 4) & 0xF
    right = x & 0xF
    out = (sbox(left, S0) << 2) | sbox(right, S1)
    p4out = 0
    for i in range(4):
        p4out <<= 1
        p4out |= (out >> (3 - P4[i])) & 1
    return p4out

def fk(val, k1, k2):
    ip = permute(val, IP, 8)
    left = ip >> 4
    right = ip & 0xF
    t1 = f(right, k1)
    left ^= t1
    # Swap halves
    left, right = right, left
    t2 = f(right, k2)
    left ^= t2
    preout = (left << 4) | right
    out = permute(preout, IP_INV, 8)
    return out

def ctr_mode(data, k1, k2, counter_start=0):
    output = []
    for i, block in enumerate(data):
        keystream = fk(counter_start + i, k1, k2)
        output.append(block ^ keystream)
    return output

# Example usage
plaintext = [0x01, 0x02, 0x04]
key = 0x1FD
counter = 0x00

k1, k2 = key_gen(key)
ciphertext = ctr_mode(plaintext, k1, k2, counter)
decrypted = ctr_mode(ciphertext, k1, k2, counter)

print("Encrypted:", [f"{b:02X}" for b in ciphertext])
print("Decrypted:", [f"{b:02X}" for b in decrypted])
