# What will be the GCD?

# Problem Statement
# Write a program where you have to find the GCD(Greatest Common Divisor) of two numbers.

# Input
# The input consists of two integer numbers.

# Output
# The output will be an integer number.

# Constraints
# 0 ≤ |S| ≤ 109
# Example:
# Enter two numbers.

# Input:
# 9 12
# Output:
# 3

# GCD(a, b) = (a × b) / LCM(a, b)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

s =  input()
parts = s.split()
print(gcd(int(parts[0]), int(parts[1])))