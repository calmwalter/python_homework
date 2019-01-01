import turtle
import random
turtle.Turtle().screen.delay(0)
turtle.hideturtle()
cnt=1000
c=0
turtle.penup()
turtle.goto((-100,100))
turtle.pendown()
turtle.goto((100,100))
turtle.goto((100,-100))
turtle.goto((-100,-100))
turtle.goto((-100,100))
turtle.penup()
turtle.goto((0,0))
turtle.pendown()
turtle.goto((0,100))
turtle.penup()
turtle.goto((0,0))
turtle.pendown()
turtle.goto((100,0))
turtle.penup()
turtle.goto((0,0))
turtle.pendown()
turtle.goto((0,-100))
turtle.penup()
turtle.goto((0,100))
turtle.pendown()
turtle.goto((100,0))
turtle.pensize(5)
for i in range(cnt):
    x=random.randint(-100,101)
    y=random.randint(-100,101)
    turtle.penup()
    turtle.goto((x,y))
    turtle.pendown()
    turtle.goto((x,y))
    turtle.penup()
    if x>0 and y>0 and x+y<100:
        c+=1

turtle.goto((-100,110))
turtle.write("The possibility of the odd-region is %.2f%%"%(c/cnt*100))
turtle.done()
