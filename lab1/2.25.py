import turtle
x = eval(input("x= "))
y = eval(input("y= "))
length = eval(input("length= "))
width = eval(input("width= "))
turtle.penup()
turtle.goto((x, y))
turtle.forward(length/2)
turtle.right(90)
turtle.forward(width/2)
turtle.pendown()
x = 0
while x is not 4:
    turtle.right(90)
    if x % 2 is 0:
        turtle.forward(length)
    else:
        turtle.forward(width)
    x = x+1
turtle.done()
