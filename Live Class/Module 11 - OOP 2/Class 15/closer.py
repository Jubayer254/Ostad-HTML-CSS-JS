def outer_func(x):
    def inner_func(y): 
        return x + y
    return inner_func

add_five = outer_func(5)
print(add_five(3))
print(add_five(5))


def make_counter():
    count = 0
    def counter():
        nonlocal count # nonlocal -> to get the variable of outer function
        count += 1
        return count
    return counter

counter1 = make_counter()
print(counter1())
print(counter1())
print(counter1())
print(counter1())
print(counter1())
print(counter1())
print(counter1())
print(counter1())