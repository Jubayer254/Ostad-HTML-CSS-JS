# PATTERN
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("\n")

print("-------------------------------")

# COUNT OF DIGITS
a = 5678
a = str (a)
print("Count", len(a))

print("-------------------------------")

# COUNT OF DIGITS
import math
n = 5679
count = 0
while (n != 0):
    count += 1
    n = math.floor(n/10)
print("Count", count)

print("-------------------------------")

# SUM OF DIGITS
import math
n = 5679
sum = 0
while (n != 0):
    sum += math.floor(n%10)
    n = math.floor(n/10)
print("Sum", sum)

print("-------------------------------")

# Recurssive SUM (0-10)
def sum (number):
    if number:
        return number + sum(number - 1)
    return 0

print(sum(5))
    

    
    
