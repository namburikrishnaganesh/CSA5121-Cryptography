def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return result


q = 23     # prime number
a = 5      # primitive root
x = 6      # Alice's private key
y = 15     # Bob's private key

A = mod_exp(a, x, q)  # Alice sends this
B = mod_exp(a, y, q)  # Bob sends this

K_alice = mod_exp(B, x, q)  # Alice computes shared key
K_bob = mod_exp(A, y, q)    # Bob computes shared key

print(f"Public values: a = {a}, q = {q}")
print(f"Alice sends: {A}")
print(f"Bob sends: {B}")
print(f"Shared secret computed by Alice: {K_alice}")
print(f"Shared secret computed by Bob:   {K_bob}")
