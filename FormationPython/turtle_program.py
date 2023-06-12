import turtle

t = turtle.Turtle()

long = 100
large = 50
i = 0
j = 0
while j < 10:
    t.forward(i + long)
    t.left(90)
    t.forward(i + large)
    t.left(90)
    t.forward(i + long)
    t.left(90)
    t.forward(i + large)

turtle.done()