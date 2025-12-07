# DES Key Schedule Generation in Python (Equivalent to your C Code)

# Shift schedule for DES
shift_schedule = [
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]

# PC1 permutation table
PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

# PC2 permutation table
PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]


def permute(input_bits, table):
    """Applies permutation table to bit string."""
    return "".join(input_bits[i - 1] for i in table)


def left_shift(bits, shift):
    """Circular left shift."""
    return bits[shift:] + bits[:shift]


def main():
    key64 = input("Enter 64-bit binary key (no spaces): ").strip()

    if len(key64) != 64 or any(c not in "01" for c in key64):
        print("Invalid key! Must be exactly 64 binary bits.")
        return

    # Apply PC1 → 56-bit key
    key56 = permute(key64, PC1)

    # Split into halves
    C = key56[:28]
    D = key56[28:]

    round_keys = []

    # Generate 16 subkeys
    for i in range(16):
        C = left_shift(C, shift_schedule[i])
        D = left_shift(D, shift_schedule[i])

        CD = C + D
        sub_key = permute(CD, PC2)

        round_keys.append(sub_key)

    print("\nDES Subkeys (C-part | D-part):")
    for i, key in enumerate(round_keys):
        print(f"K{i + 1:02d}: {key[:24]} | {key[24:]}")


if __name__ == "__main__":
    main()
