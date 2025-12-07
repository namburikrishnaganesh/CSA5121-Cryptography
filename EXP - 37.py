import string

ALPHABET_SIZE = 26
MAX_RESULTS = 10
english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def analyze_frequency(text):
    freq = {ch: 0 for ch in string.ascii_uppercase}
    for ch in text:
        if ch.isalpha():
            freq[ch.upper()] += 1
    # Convert to list of tuples and sort by count descending
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq

def generate_mapping(freq_list, offset):
    mapping = {}
    for i, (letter, _) in enumerate(freq_list):
        if i + offset < ALPHABET_SIZE:
            mapping[letter] = english_freq[i + offset]
        else:
            mapping[letter] = letter  # fallback
    return mapping

def apply_mapping(ciphertext, mapping):
    output = []
    for ch in ciphertext:
        if ch.isalpha():
            upper = ch.upper()
            subst = mapping.get(upper, upper)
            output.append(subst.lower() if ch.islower() else subst)
        else:
            output.append(ch)
    return ''.join(output)

def main():
    ciphertext = input("Enter the ciphertext (letters only):\n")
    topN = int(input("Enter number of top possible plaintexts to display: "))
    if topN > MAX_RESULTS:
        topN = MAX_RESULTS

    freq_list = analyze_frequency(ciphertext)

    print(f"\nTop {topN} possible plaintexts:\n")
    for i in range(topN):
        mapping = generate_mapping(freq_list, i)
        plaintext = apply_mapping(ciphertext, mapping)
        print(f"Option {i + 1}:\n{plaintext}\n")

if __name__ == "__main__":
    main()
