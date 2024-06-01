s = set()
s.add(1)
s.add(2)
s.add(1)
print(s)

# Define two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union of set1 and set2 (all unique elements from both sets)
set_union = set1 | set2
print("Union of set1 and set2:", set_union)

# Intersection of set1 and set2 (elements common to both sets)
set_intersection = set1 & set2
print("Intersection of set1 and set2:", set_intersection)

# Difference of set1 and set2 (elements in set1 but not in set2)
set_difference = set1 - set2
print("Difference of set1 and set2:", set_difference)

# Symmetric difference of set1 and set2 (elements in either set1 or set2 but not in both)
set_symmetric_difference = set1 ^ set2
print("Symmetric difference of set1 and set2:", set_symmetric_difference)

li = [1, 2, 1, 3, 3, 4, 5]
li = set(li)
print(li) # Removes the duplicate
