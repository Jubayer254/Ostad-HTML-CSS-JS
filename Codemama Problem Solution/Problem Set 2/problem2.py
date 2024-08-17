# Reverse the Number

# Problem Statement
# Write a program where user will give a number. You will reverse the number and print it.

# Input
# The input consists of an integer number.

# Output
# The output will be the reverse of the integer number.

# Constraints
# 0 ≤ |S| ≤ 109
# Example:
# Enter number.

# Input:
# 1234
# Output:
# 4321

import math 

s =  int(input())
li = []

for x in range(len(str(s))):
    d = s % 10
    li.append(math.floor(d))
    s = s / 10

result = int(''.join(map(str, li)))
print(result)