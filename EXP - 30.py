def block_cipher(block, key):
    """Simple XOR-based block cipher"""
    return bytes([block[i] ^ key[i] for i in range(16)])


def cbc_mac(key, message, blocks):
    prev = bytes([0] * 16)  # IV = zero
    for b in range(blocks):
        block = message[b*16:(b+1)*16]

        # XOR with previous
        xored = bytes([block[i] ^ prev[i] for i in range(16)])

        # Encrypt
        prev = block_cipher(xored, key)

    return prev


def print_block(label, block):
    print(f"{label}: ", end="")
    print(" ".join(f"{b:02X}" for b in block))


def main():
    # Key
    key = bytes([0x0F] * 16)

    # Message X
    X = bytes([
        0x10, 0x11, 0x12, 0x13,
        0x14, 0x15, 0x16, 0x17,
        0x18, 0x19, 0x1A, 0x1B,
        0x1C, 0x1D, 0x1E, 0x1F
    ])

    # MAC(X)
    T = cbc_mac(key, X, 1)
    print_block("CBC-MAC of X", T)

    # Construct forged second block = X ⊕ T
    second_block = bytes([X[i] ^ T[i] for i in range(16)])
    two_block_msg = X + second_block  # Concatenated forged message

    # MAC(X || forged block)
    T2 = cbc_mac(key, two_block_msg, 2)
    print_block("CBC-MAC of X || (X⊕T)", T2)

    if T == T2:
        print("\n⚠️ Vulnerability demonstrated: MAC(X) == MAC(X || (X⊕T))")
    else:
        print("\n✅ Secure (but CBC-MAC normally isn't without protection)")


if __name__ == "__main__":
    main()
