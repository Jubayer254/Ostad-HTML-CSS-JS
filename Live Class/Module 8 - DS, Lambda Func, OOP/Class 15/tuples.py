# SWAP TUPLES
# [(1, 2), (3, 4)] -> [(2, 1), (4, 3)]

# test =  [(1, 2), (3, 4)]
# for x, y in test:
#     print(x, y)

def swap_touples(t_list):
    return [(y, x) for x, y in t_list]
print(swap_touples([(1, 2), (3, 4)]))
