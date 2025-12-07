def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

def mod_inverse(e, phi):
    gcd_val, x, y = gcd_extended(e, phi)
    if gcd_val != 1:
        return None
    else:
        return (x % phi + phi) % phi

# Given values
n = 3599
e = 31
known_plaintext = 122

# Attempt to factor n using gcd with known plaintext
factor = gcd(known_plaintext, n)
if factor == 1 or factor == n:
    print("No useful factor found.")
else:
    p = factor
    q = n // p
    print(f"Found factors: p = {p}, q = {q}")
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    print(f"φ(n) = {phi}")
    print(f"Private key d = {d}")
