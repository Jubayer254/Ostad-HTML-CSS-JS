# Calculate power of this number

# Problem Statement
# Write a program where you will be given a number and it's exponent. You will have to calculate the power of the number.

# Input
# The input consists of two integer numbers.

# Output
# The output will be an integer number.

# Constraints
# 0 ≤ |S| ≤ 109
# Example:
# Enter numbers.

# Input:
# 3 4
# Output:
# 81

def power(a, b):
    if b == 0:
        return 1
    
    p = a
    for x in range(b-1):
        p = p * a
    return p

s =  input()
parts = s.split()
print(power(int(parts[0]), int(parts[1])))