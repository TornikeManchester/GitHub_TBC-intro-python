from turtle import *

penup()
goto(-350, 100)
width(3)
color('blue')
pendown()

# Writing h
right(90)
forward(80)
circle(30, -180)

penup()
goto(-250, 65)
pendown()

circle(-30, 180)
right(90)
forward(60)
left(90)
circle(40, 90)
forward(10)

penup()
goto(-150, 100)
pendown()

right(90)
forward(80)

penup()
goto(-100, 100)
pendown()

forward(80)

penup()
goto(-70, 50)
pendown()

circle(30)



exitonclick()
