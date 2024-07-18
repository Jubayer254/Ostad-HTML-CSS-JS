def greeting(name):
    return "Hello " + name

print(greeting("Jubayer"))

# lambda argumentsz: expression
greet = lambda name: "Hello " + name 
print(greet('Saad'))

arr = [1 ,2 ,3, 4]
doubled_arr = list(map(lambda x : x*2, arr))
print(doubled_arr)