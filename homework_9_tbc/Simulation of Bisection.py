import turtle

t= turtle.Turtle()
t.width(2)
t.speed(1)

t.penup()
t.goto(-200, 0)
t.pendown()
t.forward(500)

a = 0
b = 225
epsilon = 0.01

t.color('lime')
t.penup()
t.goto(a, 0)
t.pendown()
t.dot(10)

t.penup()
t.goto(b, 0)
t.pendown()
t.dot(10)

while abs(b - a) >= epsilon:
    midpoint = (a + b) / 2
    t.penup()
    t.goto(midpoint, 0)
    t.pendown()
    t.dot(10)

    if midpoint ** 2 < (b ** 2) / 2:
        a = midpoint
    else:
        b = midpoint

turtle.done()