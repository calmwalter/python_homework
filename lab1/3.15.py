import turtle
turtle.penup()
turtle.goto((0, -100))
turtle.pendown()

turtle.circle(100)
turtle.penup()
turtle.goto((25, -20))
turtle.pendown()
x=0
while x is not 3:
    x=x+1
    turtle.left(120)
    turtle.forward(50)
def eye(pos):
    turtle.penup()
    turtle.goto(pos)
    turtle.begin_fill()
    turtle.color("black")
    turtle.pendown()
    turtle.circle(15)
    turtle.end_fill()

eye((-50,40))
eye((50,40))

turtle.penup()
turtle.goto((-85,-20))
turtle.right(30)
turtle.pendown()
turtle.forward(100)
turtle.left(60)
turtle.pendown()
turtle.forward(100)
turtle.hideturtle()

turtle.done()