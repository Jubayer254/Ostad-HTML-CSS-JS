li = [1, 4, 3, 15, 7, 45, 6]

max_li = float('-inf')

for items in li:
    if items > max_li:
        max_li = items

print("MAX: ",max_li)

min_li = float('inf')

for items in li:
    if items < min_li:
        min_li = items

print("MIN: ",min_li)

sum = 0
for items in li:
    sum += items
print("SUM: ",sum)
