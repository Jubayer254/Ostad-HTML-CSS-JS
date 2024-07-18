from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda n:n % 2 == 0, numbers))
print(even_numbers)

squared_even_nums = list(map (lambda n:n *2, even_numbers))
print(squared_even_nums)

sum_squared_even_nums = (reduce(lambda x, y: x+y, squared_even_nums))
print(sum_squared_even_nums)