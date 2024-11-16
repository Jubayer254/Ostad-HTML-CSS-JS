# String Rotation

# Problem Statement
# Write a program to create a function that checks if one string is a rotation of another.
# For example, "waterbottle" is a rotation of "erbottlewat" because you can rotate it to get the original string.

# Input
# The input consists of two strings 
# S and T

# Output
# The output will print either "True" or "False".

# Constraints
# 0 ≤ |S| ≤ 10000
# 0 ≤ |T| ≤ 10000
# Example:
# Enter strings

# Input:
# waterbottle erbottlewat
# Output:
# True

def is_rotation(S, T):
    if len(S) != len(T):
        return False

    return T in (S + S)

x = input("")

S = x.split()[0]
T = x.split()[1]

print(is_rotation(S, T))
