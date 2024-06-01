country = "bangladesh"
print(country*3)
print(country[0:3])
print(country[1])
print(country[-1])
print(country[:])
print(country.upper())
print(country.lower())
print(country.capitalize())
# country[0] = 'g' string immutable
print(country)
print(country.find("bangla"))
print(country.find("desh"))
print(country.find("ccc"))
print(country.startswith("bangla"))
print(country.endswith("desh"))
print("-----------------------------------------------------------------------------------")
c_list = country.split(",")
print(c_list)
fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Watermelon",
    "Pineapple",
    "Mango"
]
fruits_string = ", ".join(fruits)
print(fruits_string)

