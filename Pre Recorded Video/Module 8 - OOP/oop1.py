class Car:
    def __init__(self, mk, mdl, yr):
        self.make = mk
        self.model = mdl
        self.year = yr

    def move(self):
        print("The car is moving")

    def horn(self):
        print("Beep beep!")

c = Car("Toyota", "Corola", "2009")
print(c.make, c.model, c.year)
c.move()
c.horn()

c2 = Car("Subaru", "Forester", "2014")
print(c2.make, c2.model, c2.year)
c2.move()
c2.horn()