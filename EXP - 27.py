def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return result


e = 17
n = 3233
message = 2

ciphertext = mod_exp(message, e, n)
print(f"Encrypted 'C' (2): {ciphertext}")

print("\nAttacker trying brute-force:")
for m in range(26):
    test = mod_exp(m, e, n)
    print(f"Trying m = {m:2d} → {test:4d}", end="")
    if test == ciphertext:
        print(f"  ← Match! m = {m} ('{chr(ord('A') + m)}')")
    else:
        print()
