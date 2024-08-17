# Find Next Number

# Problem Statement
# Write a program where you will be given three numbers. You will have to find the next number.

# Input
# The input consists of three integer numbers.

# Output
# The output will be an integer number.

# Constraints
# 0 ≤ |S| ≤ 109
# Example:
# Enter three numbers.

# Input:
# 3 5 7
# Output:
# 9

s = input()
parts = s.split()

a = int(parts[0])
b = int(parts[1])
c = int(parts[2])

next_number = c + (c - b)

print(next_number)