import math
def area(r):
    return math.pi * r

li1 = [1, 5, 8, 30, 43]

calculated_map_area = map(area, li1)
print(list(calculated_map_area))