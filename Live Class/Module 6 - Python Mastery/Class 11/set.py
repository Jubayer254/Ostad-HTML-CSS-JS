s = {1, 2, 3, 4, 5, 6, 6, 6, 6}
s.add(7)
s.add(8)
s.add(9)
s.add(10)
print(s, type(s))

li = [1, 2, 3, 4, 5, 6, 6, 6, 6]
unq_s = set(li)
unq_li = list(unq_s)
print(unq_li)

for item in s:
    print(item)

# print(s[0]) TypeError: 'set' object is not subscriptable

text = '''The garden was a breathtaking tapestry of colors, where the red roses stood proudly
amidst a sea of blue forget-me-nots. The sunflowers added a splash of vibrant yellow, their faces
turned eagerly towards the sun. Nearby, clusters of violet lavender swayed gently in the breeze,
their soothing scent mingling with the earthy aroma of freshly turned soil. The combination of red,
blue, yellow, and violet flowers created a harmonious and visually stunning display, capturing the
essence of nature's beauty in a single, enchanting scene.'''

colors = ["red", "blue", "yellow", "violet"]

found_colors = set()

li = text.split(' ')

for words in li:
    if words in colors:
        found_colors.add(words)

print(found_colors) # got unique because of set

