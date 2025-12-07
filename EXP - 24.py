def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    gcd, x, y = gcd_extended(e, phi)
    if gcd != 1:
        return None  # No modular inverse exists
    else:
        return (x % phi + phi) % phi

# Given values
e = 31
p = 59
q = 61
n = p * q
phi = (p - 1) * (q - 1)

# Compute private key d
d = mod_inverse(e, phi)

# Print results
print(f"Public Key (e, n): ({e}, {n})")
print(f"p = {p}, q = {q}")
print(f"φ(n) = {phi}")
print(f"Private Key d = {d}")
