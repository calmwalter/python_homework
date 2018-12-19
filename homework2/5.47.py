import turtle
import random
turtle.hideturtle()
turtle.penup()
turtle.goto((-60,50))
turtle.pendown()
turtle.goto((60,50))
turtle.goto((60,-50))
turtle.goto((-60,-50))
turtle.goto((-60,50))
turtle.pensize(5)
for i in range(10):
    x=random.randint(-60,60)
    y=random.randint(-50,50)
    turtle.penup()
    turtle.goto((x,y))
    turtle.pendown()
    turtle.goto((x,y))
turtle.done()
