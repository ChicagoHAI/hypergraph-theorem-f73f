# This experiment validates properties of the Collatz conjecture (3n+1 problem) by tracking sequence lengths and maximum values reached for starting numbers in a range. We'll test the conjecture that all positive integers eventually reach 1, and analyze sequence characteristics.
# Verified: No (simulated)

import numpy as np

def collatz_sequence(n):
    """Return sequence length and maximum value for starting number n"""
    length = 1
    max_val = n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        length += 1
        max_val = max(max_val, n)
    return length, max_val

# Test range of numbers
start_range = 1
end_range = 100
lengths = []
max_values = []

print(f"Testing Collatz conjecture for numbers {start_range} to {end_range}")
print("\nSample detailed sequences:")

# Detailed analysis of a few specific numbers
for n in [7, 27, 31]:
    print(f"\nStarting number: {n}")
    curr = n
    sequence = [curr]
    while curr != 1:
        if curr % 2 == 0:
            curr = curr // 2
        else:
            curr = 3*curr + 1
        sequence.append(curr)
    print(f"Sequence: {sequence}")
    print(f"Length: {len(sequence)}")
    print(f"Maximum value: {max(sequence)}")

# Statistical analysis
for i in range(start_range, end_range + 1):
    length, max_val = collatz_sequence(i)
    lengths.append(length)
    max_values.append(max_val)

print("\nStatistical Summary:")
print(f"Average sequence length: {np.mean(lengths):.2f}")
print(f"Maximum sequence length: {max(lengths)} (for n={lengths.index(max(lengths))+1})")
print(f"Minimum sequence length: {min(lengths)} (for n={lengths.index(min(lengths))+1})")
print(f"Maximum value reached: {max(max_values)} (for n={max_values.index(max(max_values))+1})")
