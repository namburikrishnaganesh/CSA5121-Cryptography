import string

# English frequency percentages (A-Z)
englishFreq = [
    8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015,
    6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749,
    7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758,
    0.978, 2.360, 0.150, 1.974, 0.074
]

def charToIndex(c):
    return ord(c.lower()) - ord('a')

def caesarDecrypt(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            decrypted = chr((ord(ch) - ord(base) - key) % 26 + ord(base))
            result += decrypted
        else:
            result += ch
    return result

def computeScore(text):
    letterCounts = [0] * 26
    totalLetters = 0

    for ch in text:
        if ch.isalpha():
            idx = charToIndex(ch)
            if 0 <= idx < 26:
                letterCounts[idx] += 1
                totalLetters += 1

    if totalLetters == 0:
        return 0

    score = 0
    for i in range(26):
        observed = (letterCounts[i] / totalLetters) * 100
        score += englishFreq[i] * observed

    return score

def main():
    ciphertext = input("Enter ciphertext (Caesar-encrypted): ").strip()
    topN = int(input("Enter number of top probable plaintexts to display: "))

    results = []

    for key in range(26):
        plaintext = caesarDecrypt(ciphertext, key)
        score = computeScore(plaintext)
        results.append((key, score, plaintext))

    # Sort by highest score
    results.sort(key=lambda x: x[1], reverse=True)

    print("\nTop results:")
    for i in range(min(topN, 26)):
        key, score, text = results[i]
        print(f"\n[Key = {key:2d}] Score = {score:.2f}\n{text}")

if __name__ == "__main__":
    main()
