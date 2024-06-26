items = []
items.append(1)
items.append(2)
items.append("Hello")
items.append([10, 20, 30])

for item in items:
    print(item, type(item))

for i in range(0, len(items)):
    print(items[i], type(items[i]))

for index, item in enumerate(items):
    print(index, item, items[index])

li = [4, 5, 6, 7]

items += li
print(items)

items.extend(li)
print(items)

items.append(li)
print(items)

li = [[1, 2, 3], [4, 5, 6]]
print(li[1][2])

# print(dir(items))
# print(help(list.pop))
# print(help(list.copy))
# print(help(list.sort))

nums = [1, 4, 5 , 8, 10, 12, 6, 2, 3]
nums.sort(reverse=True)
print(nums)

tpl = (1, 1, 2, 3 , 4, 4)
print(tpl.count(4))
print(tpl.index(1)) 

# Swaping
a = 10
b = 5

t = a, b
c, d = b, a
print(c, d)

b, a = a, b # creates a new tuple (variables do not swaped)
print(a, b)