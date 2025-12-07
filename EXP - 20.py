BLOCK_SIZE = 8

def xor_encrypt_block(block, key):
    return bytes([block[i] ^ key[i] for i in range(BLOCK_SIZE)])

def main():
    key = bytes([1, 2, 3, 4, 5, 6, 7, 8])
    plaintext = b"ThisIsBlock1ThisIsBlock2"
    
    # Compute number of blocks
    num_blocks = len(plaintext) // BLOCK_SIZE

    print("Original Plaintext:", plaintext.decode())

    # Encrypt each block
    ciphertext = b""
    for i in range(num_blocks):
        block = plaintext[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE]
        enc_block = xor_encrypt_block(block, key)
        ciphertext += enc_block

    # Print ciphertext in hex
    print("Ciphertext (hex):", ciphertext.hex())

    # Decrypt each block
    decrypted = b""
    for i in range(num_blocks):
        block = ciphertext[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE]
        dec_block = xor_encrypt_block(block, key)
        decrypted += dec_block

    print("Decrypted Plaintext:", decrypted.decode())

if __name__ == "__main__":
    main()
