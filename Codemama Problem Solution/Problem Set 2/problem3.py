# Find Factorial

# Problem Statement
# Write a program where you will be given a number. You will have to print the factorial of that number.

# Input
# The input consists of an integer numbers.

# Output
# The output will be an integer number.

# Constraints
# 0 ≤ |S| ≤ 109
# Example:
# Enter a number.

# Input:
# 4
# Output:
# 24

s = int(input())

r = 1
if s == 0:
    r = 1
else:
    for x in range(1, s+1):
        r = r * x
print(r) 