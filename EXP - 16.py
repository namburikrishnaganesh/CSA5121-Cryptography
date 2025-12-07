import string

MAX_TEXT = 1024
ALPHABET = 26
MAX_TRIES = 26

# Frequency ranking of English letters
englishFreqOrder = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def compute_score(text):
    score = 0
    common_letters = "etaoinshrdlu"
    
    for ch in text.lower():
        if ch == ' ':
            score += 2
        if ch in common_letters:
            score += 1
    return score

def decrypt_with_key(cipher, mapping):
    plaintext = []
    for ch in cipher:
        if ch.isalpha():
            idx = ord(ch.upper()) - ord('A')
            mapped = mapping[idx]
            plaintext.append(mapped if ch.isupper() else mapped.lower())
        else:
            plaintext.append(ch)
    return "".join(plaintext)

def main():
    ciphertext = input("Enter monoalphabetic ciphertext: ").strip()
    topN = int(input("Enter number of top guesses to display: "))

    # Frequency count
    freq = {chr(i + ord('A')): 0 for i in range(ALPHABET)}
    
    for ch in ciphertext:
        if ch.isalpha():
            freq[ch.upper()] += 1

    # Sort letters by frequency
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    results = []

    for shift in range(min(MAX_TRIES, ALPHABET)):
        mapping = [''] * ALPHABET

        for i, (letter, _) in enumerate(sorted_freq):
            mapping[ord(letter) - ord('A')] = englishFreqOrder[(i + shift) % ALPHABET]

        plaintext = decrypt_with_key(ciphertext, mapping)
        score = compute_score(plaintext)
        results.append((score, plaintext))

    # Sort results by score descending
    results.sort(reverse=True, key=lambda x: x[0])

    print("\nTop possible plaintexts:")
    for i in range(min(topN, len(results))):
        score, text = results[i]
        print(f"\n[{i + 1}] Score: {score:.2f}\n{text}")

if __name__ == "__main__":
    main()
