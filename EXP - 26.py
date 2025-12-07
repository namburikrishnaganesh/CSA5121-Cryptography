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
        return -1
    return (x % phi + phi) % phi

# Original RSA parameters
p = 61
q = 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17
d = mod_inverse(e, phi)

print("Original Keys:")
print(f"Public Key: (e={e}, n={n})")
print(f"Private Key: (d={d}, n={n})")

# New key using same n
new_e = 31
new_d = mod_inverse(new_e, phi)

print("\nNew Keys Using Same n:")
print(f"New Public Key: (e={new_e}, n={n})")
print(f"New Private Key: (d={new_d}, n={n})")

print("\n❗ Since the attacker knows original d, they can recover φ(n), factor n, and recompute any future keys.")
print("➡️ Bob MUST generate new p, q (and thus a new n) for secure keys.")
