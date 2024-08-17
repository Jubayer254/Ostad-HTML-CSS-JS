# Search for Vowels

# Problem Statement
# Write a program to check if there is a vowel in a string.

# Input
# The input consists of a string.

# Output
# Output will be the answer whether there is a vowel or not.
# If there is vowel it will print "The string contains a vowel.", otherwise it will print "The string does not contain any vowel."

# Constraints
# The program will terminate whenever it finds a vowel.
# Example-1:
# Enter a String

# Input:
# Hello
# Output:
# The string contains a vowel.
# Example-2:
# Enter a String

# Input:
# BCDFGHJKLMNPQRSTVWXYZ
# Output:
# The string does not contain any vowel.

s = input()
s_lower = s.lower()

has_vowel = False
vowels = ['a', 'e', 'i', 'o', 'u']

for char in s_lower:
    if char in vowels:
        has_vowel = True
        break

if has_vowel:
    print("The string contains a vowel.")
else:
    print("The string does not contain any vowel.")