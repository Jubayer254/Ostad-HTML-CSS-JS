text = '''The garden was a breathtaking tapestry of colors, where the red roses stood proudly
amidst a sea of blue forget-me-nots. The sunflowers added a splash of vibrant yellow, their faces
turned eagerly towards the sun. Nearby, clusters of violet lavender swayed gently in the breeze,
their soothing scent mingling with the earthy aroma of freshly turned soil. The combination of red,
blue, yellow, and violet flowers created a harmonious and visually stunning display, capturing the
essence of nature's beauty in a single, enchanting scene.'''

colors = ["red", "blue", "yellow", "violet"]

dt = {}

li = text.split(' ')

for word in li:
    if word in colors:
        if word not in dt.keys():
            dt[word] = 1
        else:
            dt[word] += 1

print(dt) # got unique because of set

num_dt = {1: "One", 2: "Two", 3: "Three"}

for key, value in num_dt.items():
    print(key, value)

for t in dt.items():
    print(t, type(t))

print(num_dt[3])