BLOCK_SIZE = 128
BYTE_LEN = BLOCK_SIZE // 8
Rb_128 = 0x87


def dummy_encrypt_zeros(key):
    """
    Mimics encrypting an all-zero block by returning predictable values
    L[i] = i+1
    """
    return bytes([i + 1 for i in range(BYTE_LEN)])


def left_shift_1bit(input_bytes):
    output = bytearray(BYTE_LEN)
    carry = 0
    for i in range(BYTE_LEN - 1, -1, -1):
        output[i] = ((input_bytes[i] << 1) & 0xFF) | carry
        carry = 1 if (input_bytes[i] & 0x80) else 0
    return bytes(output)


def xor_rb(block):
    arr = bytearray(block)
    arr[-1] ^= Rb_128
    return bytes(arr)


def print_block(label, block):
    print(f"{label}: ", end="")
    print(" ".join(f"{b:02X}" for b in block))


def main():
    key = bytes([0] * BYTE_LEN)

    # Step 1: Encrypt zeros → L
    L = dummy_encrypt_zeros(key)
    print_block("L", L)

    # Step 2: Compute K1
    K1 = left_shift_1bit(L)
    if L[0] & 0x80:
        K1 = xor_rb(K1)
    print_block("K1", K1)

    # Step 3: Compute K2
    K2 = left_shift_1bit(K1)
    if K1[0] & 0x80:
        K2 = xor_rb(K2)
    print_block("K2", K2)


if __name__ == "__main__":
    main()
