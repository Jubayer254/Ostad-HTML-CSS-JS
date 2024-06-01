# TUPLE IS IMMUTABLE

tpl = (1, 2, 3, 4)
print(tpl)
print(tpl[1], tpl[-1])

for item in tpl:
    print(item)

tpl = 1, 2, 3
print(tpl, type(tpl))
print(dir(tpl))
# tpl[0] = 12 IMMUTABLE

a, b, c = tpl
print(a, b, c)
