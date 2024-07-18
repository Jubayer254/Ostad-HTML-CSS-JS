n1 = input("Enter first number:")
n2 = input("Enter second number:")

try:
    print(int(n1)/int(n2))
except ZeroDivisionError:
    print("Can not devide by 0. Please enter a non-zero number.")
except TypeError:
    print("Error!!! Please contact the programmer.")
except ValueError:
    print("Can only input number.")

# MULTIPLE EXCEPTION IN ONE LINE
try:
    # some code that may raise exceptions
    result = 10 / 0
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")