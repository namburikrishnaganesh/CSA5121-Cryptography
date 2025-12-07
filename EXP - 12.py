import string

MOD = 26

def matrix_multiply(key, pair):
    return [
        (key[0][0] * pair[0] + key[0][1] * pair[1]) % MOD,
        (key[1][0] * pair[0] + key[1][1] * pair[1]) % MOD
    ]


def mod_inverse(a):
    a %= MOD
    for x in range(1, MOD):
        if (a * x) % MOD == 1:
            return x
    return -1


def inverse_key(key):
    det = (key[0][0] * key[1][1] - key[0][1] * key[1][0]) % MOD
    inv_det = mod_inverse(det)

    if inv_det == -1:
        print("Key matrix is not invertible.")
        return None

    inv_key = [
        [(key[1][1] * inv_det) % MOD, (-key[0][1] * inv_det) % MOD],
        [(-key[1][0] * inv_det) % MOD, (key[0][0] * inv_det) % MOD]
    ]

    # Make sure values are positive
    for i in range(2):
        for j in range(2):
            inv_key[i][j] %= MOD
    
    return inv_key


def preprocess(input_text):
    output = ""
    for ch in input_text:
        if ch.isalpha():
            ch = ch.upper()
            if ch == 'J':
                ch = 'I'
            output += ch

    if len(output) % 2 != 0:
        output += 'X'

    return output


def encrypt_hill(message, key):
    print("\nEncrypted Text:")
    for i in range(0, len(message), 2):
        pair = [ord(message[i]) - ord('A'),
                ord(message[i + 1]) - ord('A')]
        
        result = matrix_multiply(key, pair)

        print(chr(result[0] + ord('A')) + chr(result[1] + ord('A')), end="")
    print()


def decrypt_hill(cipher, key):
    inv_key = inverse_key(key)
    print("\nDecrypted Text:")
    for i in range(0, len(cipher), 2):
        pair = [ord(cipher[i]) - ord('A'),
                ord(cipher[i + 1]) - ord('A')]
        
        result = matrix_multiply(inv_key, pair)

        print(chr(result[0] + ord('A')) + chr(result[1] + ord('A')), end="")
    print()


# ---- MAIN EXECUTION ----

text = "meet me at the usual place at ten rather than eight oclock"
key = [[9, 4], [5, 7]]

cleaned = preprocess(text)
print("Cleaned Message:", cleaned)

encrypt_hill(cleaned, key)

ciphertext = "KCLUBGUBDKXIJAFKXZQLNDWSJAGRLJCKYUVCDPVQGVQMLYHUG"
decrypt_hill(ciphertext, key)
