# WRITE
# fp = open("txt/myfile.txt", "w")
# fp.write("This is a test line.\n")
# fp.close()

# APPEND
# fp = open("txt/myfile.txt", "a")
# fp.write("This is a test line.\n")
# fp.close()

# ITTERABLE
fp = open("txt/myfile.txt", "w")
fruits = [
    "Apple\n",
    "Banana\n",
    "Orange\n",
    "Watermelon\n",
    "Pineapple\n",
    "Mango\n"
]
fp.writelines(fruits)
fp.close()

# READ
fp = open("txt/myfile.txt", "r")
content = fp.read()
print(content)
print(type(content))
fp.close()

# CONTEXT MANAGER
with open("txt/myfile.txt", "r") as fp:
    content = fp.read()
    print(content)

with open("txt/myfile.txt", "r") as fp:
    content = fp.readlines()
    print(content)