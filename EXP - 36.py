def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1  # no inverse

def encrypt_char(ch, a, b):
    if ch.isalpha():
        ch = ch.upper()
        p = ord(ch) - ord('A')
        c = (a * p + b) % 26
        return chr(c + ord('A'))
    return ch

def decrypt_char(ch, a, b):
    if ch.isalpha():
        ch = ch.upper()
        a_inv = mod_inverse(a, 26)
        if a_inv == -1:
            return '?'  # no inverse exists
        c = ord(ch) - ord('A')
        p = (a_inv * (c - b + 26)) % 26
        return chr(p + ord('A'))
    return ch

# ----------- MAIN Program -------------
a = int(input("Enter value of a (must be coprime with 26): "))
b = int(input("Enter value of b: "))

if gcd(a, 26) != 1:
    print("Invalid 'a' value! It must be coprime with 26.")
    exit()

plaintext = input("Enter the plaintext (letters only): ")

# Encryption
ciphertext = ''.join(encrypt_char(ch, a, b) for ch in plaintext)
print("Encrypted Text:", ciphertext)

# Decryption
decrypted = ''.join(decrypt_char(ch, a, b) for ch in ciphertext)
print("Decrypted Text:", decrypted)
