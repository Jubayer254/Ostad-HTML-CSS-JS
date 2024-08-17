# Check for Palindrome

# Problem Statement
# Write a program to check whether a number is palindrome or not.
# palindrome Number: A palindromic number is a number (such as 16461) that remains the same when its digits are reversed.

# Input
# The input consists of an integer number.

# Output
# The output will print whether the input is palindrome number or not.

# Constraints
# 0 ≤ |S| ≤ 109
# Example-1:
# Enter number

# Input:
# 121
# Output:
# 121 is a palindrome number
# Example-2:
# Enter number

# Input:
# 123
# Output:
# 123 is not a palindrome number

s = input()

s_rev = s[::-1]

if int(s) == int(s_rev):
    print(f"{s} is a palindrome number")
else:
    print(f"{s} is not a palindrome number")