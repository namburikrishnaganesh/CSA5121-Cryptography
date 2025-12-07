matrix = [
    ['M', 'F', 'H', 'I', 'K'],
    ['U', 'N', 'O', 'P', 'Q'],
    ['Z', 'V', 'W', 'X', 'Y'],
    ['E', 'L', 'A', 'R', 'G'],
    ['D', 'S', 'T', 'B', 'C']
]

SIZE = 5

def find_position(ch):
    if ch == 'J':
        ch = 'I'
    for i in range(SIZE):
        for j in range(SIZE):
            if matrix[i][j] == ch:
                return i, j
    return None, None

def encrypt_pair(a, b):
    row1, col1 = find_position(a)
    row2, col2 = find_position(b)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % SIZE], matrix[row2][(col2 + 1) % SIZE]
    elif col1 == col2:
        return matrix[(row1 + 1) % SIZE][col1], matrix[(row2 + 1) % SIZE][col2]
    else:
        return matrix[row1][col2], matrix[row2][col1]

def prepare_text(text):
    clean = []

    for ch in text:
        if ch.isalpha():
            clean.append(ch.upper().replace('J', 'I'))

    pairs = []
    i = 0
    while i < len(clean):
        a = clean[i]
        b = clean[i + 1] if i + 1 < len(clean) else 'X'
        if a == b:
            b = 'X'
            i += 1
        else
            i += 2
        pairs.append((a, b))
    return pairs
def encrypt_message(text):
    pairs = prepare_text(text)
    print("Encrypted Message:")
    result = ""
    for a, b in pairs:
        c1, c2 = encrypt_pair(a, b)
        result += c1 + c2
    print(result)
def main():
    message = "Must see you over Cadogan West. Coming at once."
    print("Original Message:")
    print(message)
    print()
    encrypt_message(message)
main()
