numbers = input("Enter the number comma(,) seperated: ")
input_list = numbers.split(",")

print("Odd Numbers:")
for num in input_list:
    if(int(num) % 2 != 0):
        print(int(num))
