# DES Key Scheduling in Python

# Shift schedule (same as in C)
shift_schedule = [
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]

# PC1 permutation
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

# PC2 permutation
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
    """ Apply permutation table to input bit string """
    return "".join(input_bits[i - 1] for i in table)


def left_shift(bits, shift):
    """ Circular left shift for DES key halves """
    return bits[shift:] + bits[:shift]


def main():
    initial_key = input("Enter 64-bit key (in binary, no spaces): ").strip()

    if len(initial_key) != 64 or any(c not in "01" for c in initial_key):
        print("Invalid key! Must be 64 bits of 0s and 1s.")
        return

    # Apply PC1 permutation — gets 56-bit key
    permuted_key = permute(initial_key, PC1)

    # Split into C and D
    C = permuted_key[:28]
    D = permuted_key[28:]

    round_keys = []

    # Generate 16 round keys
    for i in range(16):
        C = left_shift(C, shift_schedule[i])
        D = left_shift(D, shift_schedule[i])

        combined = C + D
        round_key = permute(combined, PC2)

        round_keys.append(round_key)

    print("\nDES Decryption Round Keys (K16 to K1):")
    for i in range(15, -1, -1):
        print(f"K{16 - i:02d}: {round_keys[i]}")


if __name__ == "__main__":
    main()
