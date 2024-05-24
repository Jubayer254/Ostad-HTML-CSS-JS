year = input("Enter a Year: ")
year = int(year)

if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
