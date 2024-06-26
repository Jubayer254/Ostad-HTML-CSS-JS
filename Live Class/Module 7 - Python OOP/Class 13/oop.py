class Maths:
    def __init__(self) :
        print("Obj Created")

    className = "This is a Maths class"

    def add(self, i, j):
        return i + j
    
    def substract(self, i, j):
        return i - j
    
    def testsub(self):
        return self.substract(30, 20)
    
m = Maths()
sum = m.add(5, 9)
print(sum)
subs = m.substract(6, 2)
print(subs)
print(m.className)

n = Maths()
sum = n.add(5, 9)
print(sum)
subs = n.substract(6, 2)
print(subs)

print(m.testsub())

# Constractor

class Person:
    def __init__(self, s):
        self.name = s 

    def hello(self):
        print("Hello", self.name)

t = Person("Jubayer")
t.hello()

# Class Inheritence

class Shape():
    def __init__(self):
        self.color = (0, 0, 0)

class Rectangle(Shape):
    def __init__(self, w, h):
        Shape.__init__(self) # Need to call constructor from super class
        self.width = w
        self.height = h
    
    def area(self):
        return self.width * self.height
    
r = Rectangle(5, 7)
print(r.area())
print(r.height)
print(r.width)
print(r.color)
