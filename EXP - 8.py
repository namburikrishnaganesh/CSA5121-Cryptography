ALPHABET_LEN = 26
def generate_cipher_alphabet(keyword):
    used = [0] * ALPHABET_LEN
    cipher = []
    for ch in keyword.upper():
        if 'A' <= ch <= 'Z' and not used[ord(ch) - ord('A')]:
            cipher.append(ch)
            used[ord(ch) - ord('A')] = 1
    for i in range(ALPHABET_LEN):
        if not used[i]:
            cipher.append(chr(ord('A') + i))
    return ''.join(cipher)
def encrypt(plaintext, cipher):
    ciphertext = ""
    for ch in plaintext:
        lower = ch.lower()
        if 'a' <= lower <= 'z':
            ciphertext += cipher[ord(lower) - ord('a')]
        else:
            ciphertext += ch
    return ciphertext
keyword = "CIPHER"
cipher = generate_cipher_alphabet(keyword)
print("Generated Cipher Alphabet:")
print("Plain : ", ' '.join(chr(ord('A') + i) for i in range(ALPHABET_LEN)))
print("Cipher:", ' '.join(cipher))
plaintext = input("\nEnter plaintext: ")
ciphertext = encrypt(plaintext, cipher)
print("Encrypted text:", ciphertext)
