# return even number of list 
def even_list(numbers):
    even_numbers =  []

    for x in numbers:
        if x % 2 == 0:
            even_numbers.append(x)
    return even_numbers

nums = even_list([2, 3, 5, 3, 6, 7, 10])
print(f"Even Numbers: {nums}")

# WITH LAMBDA FUNC
def even_list_new(numbers):
    even_numbers =  [num for num in numbers if num % 2 == 0]
    return even_numbers

nums = even_list_new([2, 3, 5, 3, 6, 7, 10])
print(f"Even Numbers: {nums}")

# Make all the elements of a list reversed

# word = 'Django'
# print(word[::-1])

def rev_list_el(words):
    return [word[::-1] for word in words]

print(rev_list_el(['jubayer', 'django', 'MERN']))