import string
def generate_matrix(key):
    key = key.upper().replace("J", "I")
    used = set()
    seq = []
    for c in key:
        if c in string.ascii_uppercase and c not in used:
            seq.append(c)
            used.add(c)
    for c in string.ascii_uppercase:
        if c != "J" and c not in used:
            seq.append(c)
            used.add(c)
    matrix = [seq[i:i+5] for i in range(0, 25, 5)]
    return matrix
def format_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(c for c in text if c in string.ascii_uppercase)
    res = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else ""
        if a == b:
            res += a + "X"
            i += 1
        else:
            if b:
                res += a + b
                i += 2
            else:
                res += a + "X"
                i += 1
    return res
def pos(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c
def encrypt_pair(a, b, m):
    r1, c1 = pos(m, a)
    r2, c2 = pos(m, b)
    if r1 == r2:
        return m[r1][(c1+1)%5] + m[r2][(c2+1)%5]
    if c1 == c2:
        return m[(r1+1)%5][c1] + m[(r2+1)%5][c2]
    return m[r1][c2] + m[r2][c1]
def encrypt(text, m):
    out = ""
    for i in range(0, len(text), 2):
        out += encrypt_pair(text[i], text[i+1], m)
    return out
key = input("ENTER KEYWORD: ")
plaintext = input("ENTER PLAINTEXT: ")
matrix = generate_matrix(key)
formatted = format_text(plaintext)
cipher = encrypt(formatted, matrix)
print("\nPLAYFAIR MATRIX:")
for row in matrix:
    print(" ".join(row))
print("\nFORMATTED P.T:", formatted)
print("ENCRYPTED C.T:", cipher)
