BLOCK_SIZE = 8

def xor_encrypt(block, key):
    return bytes([block[i] ^ key[i] for i in range(BLOCK_SIZE)])

def xor_blocks(in1, in2):
    return bytes([in1[i] ^ in2[i] for i in range(BLOCK_SIZE)])

def main():
    key = bytes([1, 2, 3, 4, 5, 6, 7, 8])
    iv = bytes([0xAA, 0xBB, 0xCC, 0xDD, 0x11, 0x22, 0x33, 0x44])

    plaintext = b"CBCModeTestBlock1CBCModeTestBlock2"

    num_blocks = len(plaintext) // BLOCK_SIZE

    print("Plaintext:", plaintext.decode())

    ciphertext = b""
    prev = iv

    # CBC ENCRYPTION
    for i in range(num_blocks):
        block = plaintext[i * BLOCK_SIZE:(i + 1) * BLOCK_SIZE]
        xored = xor_blocks(block, prev)
        enc = xor_encrypt(xored, key)
        ciphertext += enc
        prev = enc

    # Print Ciphertext in Hex
    print("Ciphertext (hex):", ciphertext.hex())

    # CBC DECRYPTION
    decrypted = b""
    prev = iv

    for i in range(num_blocks):
        block = ciphertext[i * BLOCK_SIZE:(i + 1) * BLOCK_SIZE]
        temp = xor_encrypt(block, key)
        dec = xor_blocks(temp, prev)
        decrypted += dec
        prev = block

    print("Decrypted Text:", decrypted.decode())


if __name__ == "__main__":
    main()
