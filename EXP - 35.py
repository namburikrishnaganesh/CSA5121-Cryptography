import random
import string

MAX_LEN = 1024

def encrypt_char(c, key):
    if c.isupper():
        return chr(((ord(c) - ord('A') + key) % 26) + ord('A'))
    elif c.islower():
        return chr(((ord(c) - ord('a') + key) % 26) + ord('a'))
    return c

def decrypt_char(c, key):
    if c.isupper():
        return chr(((ord(c) - ord('A') - key + 26) % 26) + ord('A'))
    elif c.islower():
        return chr(((ord(c) - ord('a') - key + 26) % 26) + ord('a'))
    return c


# ----------- MAIN Equivalent Program -------------

plaintext = input("Enter plaintext (letters only): ")

random.seed()  # auto seed

ciphertext = []
decrypted = []
key = []

for ch in plaintext:
    if ch.isalpha():
        k = random.randint(0, 26)  # random key between 0–26
        key.append(k)
        ciphertext.append(encrypt_char(ch, k))
    else:
        key.append(0)
        ciphertext.append(ch)

ciphertext = "".join(ciphertext)

for i, ch in enumerate(ciphertext):
    decrypted.append(decrypt_char(ch, key[i]))

decrypted = "".join(decrypted)

print("\nGenerated key:", end=" ")
for i, ch in enumerate(plaintext):
    if ch.isalpha():
        print(key[i], end=" ")
    else:
        print("_", end=" ")

print("\nCiphertext:", ciphertext)
print("Decrypted :", decrypted)
