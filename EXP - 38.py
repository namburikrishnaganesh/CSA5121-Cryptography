MOD = 26

def mod_inverse(a, m):
    a %= m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def determinant(matrix):
    return (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) % MOD

def inverse_matrix(matrix):
    det = determinant(matrix)
    det = det % MOD
    det_inv = mod_inverse(det, MOD)
    if det_inv == -1:
        return None
    inv = [
        [ matrix[1][1] * det_inv % MOD, -matrix[0][1] * det_inv % MOD ],
        [ -matrix[1][0] * det_inv % MOD, matrix[0][0] * det_inv % MOD ]
    ]
    for i in range(2):
        for j in range(2):
            if inv[i][j] < 0:
                inv[i][j] += MOD
    return inv

def multiply_matrix(a, b):
    result = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            val = 0
            for k in range(2):
                val += a[i][k] * b[k][j]
            result[i][j] = val % MOD
    return result

def text_to_matrix(text):
    text = text.upper()
    return [[ord(text[0])-ord('A'), ord(text[1])-ord('A')],
            [ord(text[2])-ord('A'), ord(text[3])-ord('A')]]

def encrypt(pt, key):
    pt_nums = [ord(pt[0].upper()) - ord('A'), ord(pt[1].upper()) - ord('A')]
    ct_nums = [
        (key[0][0]*pt_nums[0] + key[0][1]*pt_nums[1]) % MOD,
        (key[1][0]*pt_nums[0] + key[1][1]*pt_nums[1]) % MOD
    ]
    return ''.join([chr(n + ord('A')) for n in ct_nums])

# Known plaintext-ciphertext
plaintext = "HELP"
ciphertext = "IZWX"

P = text_to_matrix(plaintext)
C = text_to_matrix(ciphertext)

print("Known plaintext matrix:")
for row in P:
    print(row)
print("Known ciphertext matrix:")
for row in C:
    print(row)

P_inv = inverse_matrix(P)
if P_inv is None:
    print("Matrix inversion failed. Plaintext matrix is not invertible mod 26.")
    exit(1)

Key = multiply_matrix(C, P_inv)
print("Recovered Key Matrix:")
for row in Key:
    print(row)

# Test encryption
test = "HI"
encrypted = encrypt(test, Key)
print(f"Test Encryption of '{test}': {encrypted}")
