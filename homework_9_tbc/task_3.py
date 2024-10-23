import turtle
import random
import math

t = turtle.Turtle()
t.color('blue')
t.width(1)
t.speed(100)

# x-axis
t.penup()
t.goto(0, 0)
t.pendown()
t.forward(500)

t.setheading(0)
t.forward(10)
t.right(150)
t.forward(20)
t.back(20)
t.left(300)
t.forward(20)

# y-axis
t.penup()
t.goto(0, 0)
t.pendown()
t.right(60)
t.forward(200)

t.setheading(90)
t.forward(100)
t.right(150)
t.forward(20)
t.back(20)
t.left(300)
t.forward(20)

t.penup()
t.goto(0, 0)
t.pendown()
t.left(30)
t.forward(300)

# x-axis negatives
t.penup()
t.goto(0,0)
t.pendown()
t.right(90)
t.forward(500)

# circle
t.penup()
t.goto(0, 100)
t.pendown()
t.color('black')
t.circle(100)

# dots outside the circle
num_points = 200
for i in range(num_points):
    a = random.uniform(-3, 3)
    b = random.uniform(-3, 3)
    x = a * 100
    y = b * 100

    if math.sqrt(a ** 2 + b ** 2) <= 1:
        t.color('red')
    else:
        t.color('green')

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(5)

t.hideturtle()
turtle.done()