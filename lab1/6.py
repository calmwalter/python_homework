import turtle
x=0
turtle.penup()
turtle.goto((-250,0))
turtle.pendown()
turtle.begin_fill()
while x is not 36:
    x=x+1
    turtle.forward(500) 
    turtle.left(170)
turtle.color("yellow")
turtle.end_fill()
turtle.hideturtle()
turtle.done()