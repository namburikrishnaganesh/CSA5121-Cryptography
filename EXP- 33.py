# DES‑like toy implementation in Python

IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# Fixed key
key = 0x133457799BBCDFF1


def feistel(half, subkey):
    return half ^ (subkey & 0xFFFFFFFF)


def permute(value, table):
    output = 0
    for pos in table:
        output <<= 1
        output |= (value >> (64 - pos)) & 1
    return output


def des_process(block, encrypt=True):
    permuted = permute(block, IP)

    L = (permuted >> 32) & 0xFFFFFFFF
    R = permuted & 0xFFFFFFFF

    for round_num in range(16):
        shift = round_num if encrypt else (15 - round_num)
        subkey = key >> shift

        temp = R
        R = L ^ feistel(R, subkey)
        L = temp

    pre_output = (R << 32) | L
    return permute(pre_output, FP)


def str_to_uint64(text):
    value = 0
    for ch in text:
        value = (value << 8) | ord(ch)
    return value


def uint64_to_str(value):
    return "".join(chr((value >> (8 * i)) & 0xFF) for i in reversed(range(8)))


# Main program equivalent
plaintext = "DESDEMO!"
print("Plaintext:", plaintext)

pt_val = str_to_uint64(plaintext)
ct_val = des_process(pt_val, True)

print("Encrypted (hex): %016X" % ct_val)

dt_val = des_process(ct_val, False)
decrypted = uint64_to_str(dt_val)

print("Decrypted:", decrypted)
