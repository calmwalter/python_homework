import turtle
length=eval(input("Enter the length of the star:"))
turtle.penup()
turtle.left(36)
x=0
turtle.pendown()
while x!=5:
    turtle.forward(length)
    turtle.left(144)
    x=x+1

turtle.done() 