def outer_func(name):
    def inner_func(): 
        return f'Hello {name} from inner function'
    return(inner_func())

print(outer_func('Jubayer'))

# inner_func() # not accessible from outside