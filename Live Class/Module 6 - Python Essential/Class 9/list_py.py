items = [1, 2, 3, 4,3, "ABC"]

print(type(items))
print(len(items))
print("ABC" in items)
print("AB" in items)

for item in items:
    print(item)

country = "Bangladesh"
for c in country:
    print(c)

items[0] = "Hello"
print(items)

city = "Dhaka"
str_to_li = list(city)
print(str_to_li)
str_to_li[0] = 'B'
print(str_to_li)

li_to_str = "-".join(str_to_li)
print(li_to_str)

print(items[-1])