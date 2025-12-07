SIZE = 5
matrix = [[None] * SIZE for _ in range(SIZE)]
def generate_key_matrix(key):
    used = [0] * 26
    k = 0
    for ch in key.upper():
        if ch == 'J':
            ch = 'I'
        if 'A' <= ch <= 'Z' and not used[ord(ch) - ord('A')]:
            matrix[k // SIZE][k % SIZE] = ch
            used[ord(ch) - ord('A')] = 1
            k += 1
    for i in range(26):
        ch = chr(i + ord('A'))
        if ch == 'J':
            continue
        if not used[i]:
            matrix[k // SIZE][k % SIZE] = ch
            used[i] = 1
            k += 1
def find_position(ch):
    if ch == 'J':
        ch = 'I'
    for i in range(SIZE):
        for j in range(SIZE):
            if matrix[i][j] == ch:
                return i, j
    return None, None
def decrypt_pair(a, b):
    row1, col1 = find_position(a)
    row2, col2 = find_position(b)
    if row1 == row2:
        return (
            matrix[row1][(col1 - 1) % SIZE],
            matrix[row2][(col2 - 1) % SIZE]
        )
    elif col1 == col2:
        return (
            matrix[(row1 - 1) % SIZE][col1],
            matrix[(row2 - 1) % SIZE][col2]
        )
    else:
        return (
            matrix[row1][col2],
            matrix[row2][col1]
        )
def decrypt_message(ciphertext):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a = ciphertext[i].upper()
        b = ciphertext[i + 1].upper()
        if a == 'J':
            a = 'I'
        if b == 'J':
            b = 'I'
        p1, p2 = decrypt_pair(a, b)
        plaintext += p1 + p2
    return plaintext
keyword = "PLAYFAIR"
ciphertext = (
    "KXJEYUREBEZWEHEWRYTUHEYFS"
    "KREHEGOYFIWTTTUOLKSYCAJPO"
    "BOTEIZONTXBYBNTGONEYCUZWR"
    "GDSONSXBOUYWRHEBAAHYUSEDQ"
)
print("Decrypting Playfair Cipher...\n")
generate_key_matrix(keyword)
decrypted = decrypt_message(ciphertext)
print("Decrypted Text:")
print(decrypted)
            
