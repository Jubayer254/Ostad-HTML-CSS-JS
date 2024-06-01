# try:
#     fp = open("txt/not_found.txt", "w")
#     fp.write("This is a test line.\n")
#     fp.close()
# except FileNotFoundError as e:
#     print("Your file is not found")

try:
    print(10/0)
except ZeroDivisionError as e:
    print("Can not divide by zero")