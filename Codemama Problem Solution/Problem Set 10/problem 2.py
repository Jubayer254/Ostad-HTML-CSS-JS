# Substitution Cipher

# Problem Statement
# A substitution cipher is a method of encryption where each letter in the plaintext is replaced by another letter according to a fixed system. One of the simplest substitution ciphers is the Caesar cipher, where each letter in the plaintext is shifted a certain number of places down or up the alphabet. You will be given a plaintext and a shift number. You will have to have to shift each letter of the plaintext according to the number.

# Input
# The program will take a string S
# S and an integer N

# Output
# The output will print a string shifted by a particular number.

# Constraints
# 0 ≤ |N| ≤ 10000
# 0 ≤ |S| ≤ 10000
# Example:
# Enter string and number

# Input:
# abcd 1
# Output:
# bcde

def caesar_cipher(text, shift):
    result = ""
    
    shift = shift % 26
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    
    return result

input_text = input("")
input_text = input_text.split()
text = input_text[0]
shift = int(input_text[1])

print(caesar_cipher(text, shift))