# key -> value

num_to_words = dict()
num_to_words = {1: "One", 2: "Two", 3: "Three"}
num_to_words[4] = "Four"
print(num_to_words, type(num_to_words))

if 1 in num_to_words:
    print(True)
else:
    print(False)

for key, value in num_to_words.items():
    print(key, value)

print(num_to_words.items())

abc = {"A": "Apple", "B": "Ball", "C": "Cat"}
print(abc.keys())
print(abc.values())
print(abc["A"])
print(abc.get("A"))

abc.clear()
print(abc)
