food = "pizza".capitalize()
print(food)
food = "pizza".lower()
print(food)
food = "pizza".upper()
print(food)
print(food[0], food[1], food[2], food[3], food[4])
print(type(food[0]), type(food[1]), type(food[2]), type(food[3]), type(food[4]))
print(food[0:2])


s = 'This is a str'
print(len(s))
print(s[len(s)-1])
print(s[-1], s[-2], s[-3])
# s[0] = 'X' string is immutable

a = 10
print(id(a))
a = 20
print(id(a))



# sum = 0
# while True:
#     num = input("Enter a number (write quit to exit): ")
#     if num == "quit":
#         break
#     num = int(num)
#     sum = sum + num
#     print(f"Sum: {sum}") 
