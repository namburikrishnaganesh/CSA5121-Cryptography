import math

def main():
    total_keys = 1
    for i in range(1, 26):
        total_keys *= i

    log2_total_keys = math.log2(total_keys)

    print(f"Total possible keys (25!): {total_keys:.0f}")
    print(f"Approximate as 2^{log2_total_keys:.0f}")
    print("Effectively unique keys (approximate): 2^61")

main()
5
