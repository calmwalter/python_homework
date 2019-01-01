import turtle


turtle.begin_fill()

turtle.color("red")
turtle.circle(100, steps=6)
turtle.end_fill()
turtle.hideturtle()
turtle.goto((-30,85))
turtle.color("white")
turtle.write("STOP",font=("Arial",18,"bold"))
turtle.done()
