MOD = 26

def mod_inverse(a):
    a %= MOD
    for x in range(1, MOD):
        if (a * x) % MOD == 1:
            return x
    return -1


def inverse_matrix(inp):
    det = (inp[0][0] * inp[1][1] - inp[0][1] * inp[1][0]) % MOD
    inv_det = mod_inverse(det)

    if inv_det == -1:
        return None

    out = [
        [(inp[1][1] * inv_det) % MOD, (-inp[0][1] * inv_det) % MOD],
        [(-inp[1][0] * inv_det) % MOD, (inp[0][0] * inv_det) % MOD]
    ]

    # Ensure positive mod values
    for i in range(2):
        for j in range(2):
            out[i][j] %= MOD

    return out


def multiply_matrix(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= MOD
    return result


def to_num(c):
    return ord(c) - ord('A')


def print_matrix(mat):
    for row in mat:
        print(f"[ {row[0]:2d} {row[1]:2d} ]")


# MAIN PROGRAM FLOW

plaintext = [
    [to_num('H'), to_num('L')],
    [to_num('E'), to_num('L')]
]

ciphertext = [
    [to_num('Z'), to_num('S')],
    [to_num('K'), to_num('U')]
]

print("Plaintext Matrix (P):")
print_matrix(plaintext)

print("\nCiphertext Matrix (C):")
print_matrix(ciphertext)

inverseP = inverse_matrix(plaintext)

if inverseP is None:
    print("\nError: Plaintext matrix is not invertible mod 26.")
else:
    print("\nInverse of Plaintext Matrix (P^-1):")
    print_matrix(inverseP)

    key = multiply_matrix(ciphertext, inverseP)
    print("\nRecovered Key Matrix (K = C * P^-1 mod 26):")
    print_matrix(key)
