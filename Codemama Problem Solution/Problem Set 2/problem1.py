# Sum of Array Elements

# Problem Statement
# Write a program where user will give an array of elements.
# You will have to print the sum of elements where each element will be less than median element.

# Input
# The input consists of size of the array and the elements of the array. Every input will be unsigned integer number.

# Output
# The output will be sum of elements that are lesser than median element.

# Constraints
# 0 ≤ |S| ≤ 109
# Example:
# Enter size of the array and the elements.

# Input:
# 6
# 30 10 5 40 60 15
# Output:
# 30

import math

n = int(input())

s =  input()
parts = s.split()
int_parts = [int(x) for x in parts]

int_parts.sort()

if n%2 != 0:
    m = int_parts[math.floor(n/2)]
else:
    m = ((int_parts[math.floor(n/2)-1]) + (int_parts[math.floor(n/2)])) / 2

sum_result = sum(p for p in int_parts if p<m)

print(sum_result)