# RETURN COMMON VALUES ONLY FROM SETS

def common_set(set1, set2):
    return set1.intersection(set2)

a = {1, 2, 3}
b = {3, 4, 5}
print(common_set(a, b))