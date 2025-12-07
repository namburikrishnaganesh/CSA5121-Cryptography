import random
import time

def hash_message(msg):
    hash_val = 0
    for ch in msg:
        hash_val = (hash_val * 31 + ord(ch)) % 10007
    return hash_val


def rsa_sign(msg, d, n):
    h = hash_message(msg)
    sig = 1
    for _ in range(d):
        sig = (sig * h) % n
    return sig


def dsa_sign(msg, private_key, q):
    h = hash_message(msg)
    k = random.randint(1, q - 1)  # Random nonce
    sig = (h * k + private_key) % q
    return sig


def main():
    random.seed(time.time())

    message = "SecureMessage"

    rsa_n = 3233
    rsa_d = 17

    dsa_private = 23
    dsa_q = 101

    print(f'Message: "{message}"\n')

    # RSA signatures
    rsa_sig1 = rsa_sign(message, rsa_d, rsa_n)
    rsa_sig2 = rsa_sign(message, rsa_d, rsa_n)

    print("RSA Signatures:")
    print(f"Signature 1: {rsa_sig1}")
    print(f"Signature 2: {rsa_sig2}")
    print("✅ RSA produces same signature for same message.\n")

    # DSA signatures
    dsa_sig1 = dsa_sign(message, dsa_private, dsa_q)
    dsa_sig2 = dsa_sign(message, dsa_private, dsa_q)

    print("DSA Signatures:")
    print(f"Signature 1: {dsa_sig1}")
    print(f"Signature 2: {dsa_sig2}")

    if dsa_sig1 != dsa_sig2:
        print("✅ DSA produces different signatures due to random nonce k.")
    else:
        print("⚠️ Unexpected result — signatures matched (rare).")


if __name__ == "__main__":
    main()
