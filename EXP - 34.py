BLOCK_SIZE = 8


def xor_cipher(input_block, key):
    return bytes([input_block[i] ^ key[i] for i in range(BLOCK_SIZE)])


def add_padding(data):
    length = len(data)
    pad_len = BLOCK_SIZE - (length % BLOCK_SIZE)
    padded = bytearray(data)
    padded.append(0x80)
    padded.extend([0x00] * (pad_len - 1))
    return padded


def ecb_encrypt(data, key):
    output = bytearray()
    for i in range(0, len(data), BLOCK_SIZE):
        block = data[i:i + BLOCK_SIZE]
        output.extend(xor_cipher(block, key))
    return output


def cbc_encrypt(data, key, iv):
    output = bytearray()
    prev = bytearray(iv)
    for i in range(0, len(data), BLOCK_SIZE):
        block = data[i:i + BLOCK_SIZE]
        xored = bytes([block[j] ^ prev[j] for j in range(BLOCK_SIZE)])
        cipher = xor_cipher(xored, key)
        output.extend(cipher)
        prev = cipher
    return output


def cfb_encrypt(data, key, iv):
    output = bytearray()
    prev = bytearray(iv)

    for i in range(0, len(data), BLOCK_SIZE):
        cipher_stream = xor_cipher(prev, key)
        block = data[i:i + BLOCK_SIZE]
        cipher = bytes([block[j] ^ cipher_stream[j] for j in range(BLOCK_SIZE)])
        output.extend(cipher)
        prev = cipher
    return output


def print_hex(label, data):
    print(f"{label}:", " ".join(f"{b:02X}" for b in data))


# ------- Main Equivalent Program ---------

key = bytes([0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x6F, 0x70, 0x81])
iv1 = bytearray([0x00] * BLOCK_SIZE)
iv2 = bytearray([0x00] * BLOCK_SIZE)
iv3 = bytearray([0x00] * BLOCK_SIZE)

message = "HELLO BLOCK WORLD!"
data = add_padding(message.encode())

ecb_out = ecb_encrypt(data, key)
cbc_out = cbc_encrypt(data, key, iv1)
cfb_out = cfb_encrypt(data, key, iv2)

print_hex("Plaintext", data)
print_hex("ECB Cipher", ecb_out)
print_hex("CBC Cipher", cbc_out)
print_hex("CFB Cipher", cfb_out)
