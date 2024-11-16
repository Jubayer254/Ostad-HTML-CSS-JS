# Calculate Square Root

# Problem Statement
# Write a program to approximate the square root of a non-negative integer using binary search.
# Your function should return an integer representing the floor of the square root.
# For example, for 6 it will print 2.

# Input
# The input consists of an integers N.

# Output
# The output will print the square root integer value of the input.

# Constraints
# 0 ≤ |N| ≤ 10000
# Example:
# Enter number

# Input:
# 6
# Output:
# 2


def integer_square_root(N):
    if N < 2:
        return N
    
    left, right = 0, N
    
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == N:
            return mid 
        elif mid * mid < N:
            left = mid + 1
            answer = mid  
        else:
            right = mid - 1
    
    return answer

N = int(input())
print(integer_square_root(N))