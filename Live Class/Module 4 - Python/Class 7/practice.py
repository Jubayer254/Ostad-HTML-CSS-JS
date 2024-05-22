# DATATYPE 
a = 10.5
b = 20
c = a+b
d = "Jubayer"
bool = True
print(type(a), type(b), type(a+b), type(d), type(bool))
print("------------------------------------------------")

# ARITHMETIC OPERATOR
a = 10
b = 4
print("a+b:", a+b)
print("a-b:", a-b)
print("a*b:", a*b)
print("a/b:", a/b)
print("a//b:", a//b) #Quotient
print("a%b:", a%b) # Remainder
print("a**b:", a**b) # Power
print("div mod:", divmod(a,b)) # Power
print("------------------------------------------------")

# LOOP
# n = input("Enter a Number: ")
# n = int(n)
# for _ in range (n):
#     print("JUBAYER")
# print("------------------------------------------------")

for number in range(2,5):
    print(number)
print("------------------------------------------------")

for number in range(5, 0, -1):
    print(number)
print("------------------------------------------------")

for number in range(1, 12, 2):
    print(number)
print("------------------------------------------------")

sum = 0
for number in range(1, 11):
    sum = sum + number
    print(sum,", ", end='')
print(".............")
print ("Total Sum: ", sum)

# Functions
def print_greetins(name): #Parameteer
    print("Assalmualaikum "+name)

print_greetins("Jubayer") #Argument
print("------------------------------------------------")

def add_two_number(a, b):
    return int(a) + int(b)

x = input("Enter the first number: ")
y = input("Enter the Second number: ")
print("Sum is:", add_two_number(x, y))
print("------------------------------------------------")