import turtle
import math
turtle.pensize(15)
turtle.penup()
x, y = pos = (-300, 0)
turtle.goto((x, 15*math.sin(x/15)))
turtle.pendown()
m = 0
while m != 600:
    x=x+1
    turtle.goto((x, 15*math.sin(x/15)))
    if m >= 150 and m<300:
        turtle.color("red")
    elif m >= 300 and m<450:
        turtle.color("orange")
    elif m >= 450:
        turtle.color("purple")
    m = m+1
turtle.done()
