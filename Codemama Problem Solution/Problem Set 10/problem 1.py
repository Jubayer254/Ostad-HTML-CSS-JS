# Remove Special Character
# Problem Statement
# Write a program to Create a function that takes a string, removes all "special" characters (e.g. ., !, @, #, $, %, ^, &, , *, (, )) and returns the new string.

# Input
# The program will take a string S

# Output
# The output will print a string without any special character.

# Constraints
# 0 ≤ |S| ≤ 1000
# Input special characters will be from (., !, @, #, $, %, ^, &, , *, (, ))
# Example:
# Enter string

# Input:
# ab!cd
# Output:
# abcd 


def remove_special_char(c):
    special_char = ['.', '!', '@', '#', '$', '%', '^', '&', ',', '*', '(', ')']
    for s in special_char:
        c = c.replace(s, '')
    return c

c = input()
print(remove_special_char(c))