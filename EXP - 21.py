BLOCK_SIZE = 8

def xor_encrypt(block, key):
    return bytes([block[i] ^ key[i] for i in range(BLOCK_SIZE)])

def xor_blocks(a, b):
    return bytes([a[i] ^ b[i] for i in range(BLOCK_SIZE)])

def pad(input_bytes):
    pad_len = BLOCK_SIZE - (len(input_bytes) % BLOCK_SIZE)
    padded = input_bytes + bytes([0x80]) + bytes([0x00] * (pad_len - 1))
    return padded

def print_hex(label, data):
    print(f"{label}: {data.hex()}")

def main():
    key = b"mysecret"       # 8 bytes
    iv  = b"initvect"       # 8 bytes
    plaintext = b"This is a test of ECB, CBC, and CFB modes."

    padded = pad(plaintext)
    padded_len = len(padded)
    print("Plaintext (padded):", padded)

    # ECB Mode
    ecb = b""
    for i in range(0, padded_len, BLOCK_SIZE):
        block = padded[i:i+BLOCK_SIZE]
        ecb += xor_encrypt(block, key)

    # CBC Mode
    cbc = b""
    prev = iv
    for i in range(0, padded_len, BLOCK_SIZE):
        block = xor_blocks(padded[i:i+BLOCK_SIZE], prev)
        block = xor_encrypt(block, key)
        cbc += block
        prev = block

    # CFB Mode
    cfb = b""
    prev = iv
    for i in range(0, padded_len, BLOCK_SIZE):
        enc = xor_encrypt(prev, key)
        block = xor_blocks(padded[i:i+BLOCK_SIZE], enc)
        cfb += block
        prev = block

    # Print results
    print_hex("ECB Mode Cipher", ecb)
    print_hex("CBC Mode Cipher", cbc)
    print_hex("CFB Mode Cipher", cfb)

if __name__ == "__main__":
    main()
