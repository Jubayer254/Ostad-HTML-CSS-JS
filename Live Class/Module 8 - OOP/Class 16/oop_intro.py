class Car:
    make = 'Toyota'
    model = 'Camry'

c1 = Car()
c2 = Car()
print(c1.make, c1.model)
print(c2.make, c2.model)

print("----------------------------------------------")

class CarV2:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    
    def update_odometer(self, om):
        if om > self.odometer:
            self.odometer = om
        else:
            print("Cannot update odometer")

    def __str__(self):
        return f"The Car is {self.make} {self.model} and the year: {self.year}"
    
    def __eq__(self, value):
        return self.make == value.make and self.model == value.model and self.year == value.year

c1 = CarV2('Toyota', 'Camry', 2023)
c2 = CarV2('Subaru', 'Forester', 2020)

print(c1.make, c1.model, c1.year)
print(c2.make, c2.model, c2.year)
print(c1)
print(c2)

print("----------------------------------------------")

print(c1.odometer)
c1.update_odometer(30)
print(c1.odometer)
c1.update_odometer(20)
print(c1.odometer)

print("----------------------------------------------")

print(c1 == c2)

c3 = CarV2('Toyota', 'Camry', 2023)
c4 = CarV2('Toyota', 'Camry', 2023)

print(c3 == c4)

print("----------------------------------------------")

class Dog:
    # mistaken use of a class variable
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog ('Fido')
e = Dog ('Buddy')
d.add_trick("Roll Over")
print(d.tricks)
print(e.tricks)
e.add_trick("Jump")
print(e.tricks)


class Animal:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print(self.name + " is Walking")
    def eat(self):
        print(self.name + " is Eating")

a1 = Animal("Snake")
a1.walk()
a1.eat()

print("----------------------------------------------")
# INHERITENCE

class Reptile(Animal):
    def eat(self):
        print("I do not eat, I bite!!!")
    def crawl(self):
        print(self.name + " is crawling")
    # pass

class Crocodile(Reptile):
    pass

class Snake(Reptile):
    atypr = 'Venomous'

a1 = Reptile("Russles Viper")
a1.eat()
a1.crawl()

s = Snake('Cobra')
s.eat()
s.crawl()
print(s.atypr)

print("----------------------------------------------")

# Private Variable
class MyClass:
    def __init__(self):
        self._internal_value = 10  # Internal variable (use with caution externally)

    def __calculate_something(self):  # Strongly private method (mangled name)
        return self._internal_value * 2

    def get_public_value(self):
        return self._internal_value * 3  # Public accessor for internal variable

# Usage
my_object = MyClass()
print(my_object.get_public_value()) 
print(my_object._internal_value) 
# print(my_object.__calculate_something) 