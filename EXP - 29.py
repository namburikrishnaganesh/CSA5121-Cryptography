import random
import time

TOTAL_LANES = 25
RATE_LANES = 16
CAPACITY_LANES = 9

def all_capacity_filled(state):
    """Check if all capacity lanes are non-zero"""
    for i in range(RATE_LANES, TOTAL_LANES):
        if state[i] == 0:
            return False
    return True

def main():
    random.seed(time.time())
    
    # Initialize state
    state = [0] * TOTAL_LANES
    for i in range(RATE_LANES):
        while True:
            state[i] = (random.getrandbits(64))
            if state[i] != 0:
                break

    # Capacity lanes initially zero
    for i in range(RATE_LANES, TOTAL_LANES):
        state[i] = 0

    rounds = 0
    while not all_capacity_filled(state):
        # Generate a random block for the rate lanes
        block = [0] * RATE_LANES
        for i in range(RATE_LANES):
            while True:
                block[i] = random.getrandbits(64)
                if block[i] != 0:
                    break

        # XOR the block with the rate lanes
        for i in range(RATE_LANES):
            state[i] ^= block[i]

        # Randomly set a bit in one of the capacity lanes
        cap_index = RATE_LANES + random.randint(0, CAPACITY_LANES - 1)
        bit_to_set = 1 << random.randint(0, 63)
        state[cap_index] |= bit_to_set

        rounds += 1

    print(f"All capacity lanes filled with nonzero bits after {rounds} rounds.")

if __name__ == "__main__":
    main()
