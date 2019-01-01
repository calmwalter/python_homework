import turtle
import math
turtle.hideturtle()
def drawPolygon(x = 0, y = 0, radius = 50, numberOfSides = 3):
    turtle.penup()
    turtle.goto((x+radius,y))
    turtle.setheading(0)
    turtle.pendown()
    turtle.left(90+180/numberOfSides)
    turtle.forward(2*radius*math.sin(math.pi/numberOfSides))
    for i in range (numberOfSides-1):
        turtle.left(360/numberOfSides)
        turtle.forward(2*radius*math.sin(math.pi/numberOfSides))
drawPolygon(-400,0,50,3)
drawPolygon(-250,0,50,4)
drawPolygon(-100,0,50,5)
drawPolygon(50,0,50,6)
drawPolygon(200,0,50,7)
drawPolygon(350,0,50,8)

turtle.done()