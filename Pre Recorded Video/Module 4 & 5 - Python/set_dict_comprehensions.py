li = [(1, "One"), (2, "Two"), (3, "Three")]
dct = {key : value for key, value in li}
print(dct)

s = 'aaaerdghhhf'
unique_l = {c for c in s}
print(unique_l)

print(type(dct), type(unique_l))

colors = [("Messi", "Blue"), ("Ronaldo", "Red"), ("Naymar", "Yellow"), ("Di Maria", "Blue"), ("Mbappe", "Blue")]
colors_dct = {color : player for color, player in colors}
print(colors_dct)
colors_set = {color for color in colors_dct.values()}
print(colors_set)