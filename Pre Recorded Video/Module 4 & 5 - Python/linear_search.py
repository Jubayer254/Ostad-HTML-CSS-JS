li = [66,43,56,75,99,48,85,79,20,56]
index = li.index(85)
print(index)

print(43 in li)

flag = 0
find = 793

for item in li:
    if item == find:
        print("Found")
        flag = 1
        break

if flag == 0: 
    print("Not Found")