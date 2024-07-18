from functools import reduce

def multiply(x, y):
    return x*y

numbers = [1, 2, 3, 4, 5]
product = reduce(multiply, numbers)

print(product) # 120

# 1 * 2 = 2
# 2 * 3 = 6
# 6 * 4 = 24
# 24 * 5 = 120
