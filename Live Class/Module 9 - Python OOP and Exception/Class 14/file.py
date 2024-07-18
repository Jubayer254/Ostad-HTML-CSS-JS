filename = "hello.py"

try:
    fp = open(filename, 'rt')
    content = fp.read()
    print(content)
    print("\n---------------------------------------\n")
    fp = open(filename, 'rt')
    content = fp.readlines()
    print(content)
    print("\n---------------------------------------\n")
    fp = open(filename, 'rt')
    content = fp.readline()
    print("1. ",content)
    content = fp.readline()
    print("2. ",content)
    content = fp.readline()
    print("3. ",content)
    content = fp.readline()
    print("4. ",content)
    content = fp.readline()
    print("5. ",content)
    print("\n---------------------------------------\n")
    fp.close()
except FileNotFoundError:
    print("Check if the filename is correct, or if the file exists")


with open(filename, 'rt') as x:
    print(x.read())

# appends the content
with open(filename, 'at') as x:
    x.write("\ne = 1000")

# remove from the contents from the file and then write
# with open(filename, 'w') as x:
#     x.write("\ne = 1000")

# read and write together
with open(filename, 'r+') as x:
    print(x.read())
    x.write('\nx=900')

#copy a file
filename = 'pic.webp'
with open(filename, 'rb') as x:
    pic = x.read()
    # print(pic)
    print(type(pic))
    
    with open('copy.webp', 'wb') as w:
        w.write(pic)