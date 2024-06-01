li = ["apple", "banana", "orange", "mango"]

fruits = []
for fruit in li:
    fruits.append(fruit.capitalize())
print(fruits)

fruits2 = [fruit.capitalize() for fruit in li]
print(fruits2)

li_len = [len(x) for x in li]
print(li_len)

cube_li = [x*x*x for x in range(1, 11)]
print(cube_li)

odd_li = [x for x in range(1, 11) if x%2 != 0]
print(odd_li)