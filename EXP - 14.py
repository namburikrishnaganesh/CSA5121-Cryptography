def char_to_num(c):
    return ord(c.lower()) - ord('a')

def num_to_char(n):
    return chr(ord('a') + n)

def encrypt_otp(plaintext, key):
    ciphertext = []
    key_index = 0   # new pointer for key

    for ch in plaintext:
        if ch == ' ':
            ciphertext.append(' ')
        else:
            p = char_to_num(ch)
            c = (p + key[key_index]) % 26
            ciphertext.append(num_to_char(c))
            key_index += 1   # move key only when letter used
    return ''.join(ciphertext)

def decrypt_otp(ciphertext, key):
    plaintext = []
    key_index = 0

    for ch in ciphertext:
        if ch == ' ':
            plaintext.append(' ')
        else:
            c = char_to_num(ch)
            p = (c - key[key_index] + 26) % 26
            plaintext.append(num_to_char(p))
            key_index += 1
    return ''.join(plaintext)

def recover_key(plaintext, ciphertext):
    key = []
    for p, c in zip(plaintext, ciphertext):
        if p == ' ':
            continue
        pn = char_to_num(p)
        cn = char_to_num(c)
        key.append((cn - pn + 26) % 26)
    return key

def print_key(key):
    print(" ".join(f"{v:2d}" for v in key))

# ================================
# Main Program
# ================================

plaintext1 = "send more money"
key1 = [9,0,1,7,23,15,21,14,11,11,2,8,9]

print("=== Part A: Encryption ===")
ciphertext1 = encrypt_otp(plaintext1, key1)

print("Plaintext :", plaintext1)
print("Key       :", end=" ")
print_key(key1)
print("Ciphertext:", ciphertext1)

print("\n=== Part B: Decryption and Key Recovery ===")

ciphertext2 = "bvnz bhed fxxmqz"
plaintext2 = "cash not needed"

recovered_key = recover_key(plaintext2, ciphertext2)

print("Plaintext :", plaintext2)
print("Ciphertext:", ciphertext2)
print("Recovered Key:", end=" ")
print_key(recovered_key)
