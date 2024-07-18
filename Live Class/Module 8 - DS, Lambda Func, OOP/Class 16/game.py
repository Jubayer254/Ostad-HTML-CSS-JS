import turtle

class NewTurtle(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('turtle')

    def forward(self, x):
        self.left(90)
        self.backward(2*x)
    
nonte = turtle.Turtle()
nonte.forward(100)

monte = NewTurtle()
monte.forward(100)


turtle.done()