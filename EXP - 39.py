import string

english_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def decrypt(cipher, key):
    plain = []
    for c in cipher:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            plain.append(chr((ord(c) - base - key) % 26 + base))
        else:
            plain.append(c)
    return ''.join(plain)

def score_text(text):
    freq = [0] * 26
    for c in text:
        if c.isalpha():
            freq[ord(c.upper()) - ord('A')] += 1
    score = 0
    for i, ch in enumerate(english_order):
        score += freq[ord(ch) - ord('A')] * (26 - i)
    return score

def main():
    ciphertext = input("Enter the ciphertext:\n")
    n = int(input("Enter how many top guesses to show (max 26): "))
    n = min(n, 26)

    candidates = []
    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        score = score_text(plaintext)
        candidates.append({'key': key, 'score': score, 'plaintext': plaintext})

    candidates.sort(key=lambda x: x['score'], reverse=True)

    print(f"\nTop {n} possible plaintexts:\n")
    for i in range(n):
        c = candidates[i]
        print(f"Option {i+1} (Key = {c['key']}):\n{c['plaintext']}\n")

if __name__ == "__main__":
    main()
