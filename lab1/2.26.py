import turtle
x=eval(input("x="))
y=eval(input("y="))
r=eval( input("Enter the radius:"))
PI=3.1415926535
turtle.penup()
turtle.goto((x,y-r))
turtle.pendown()
turtle.circle(r)
turtle.penup()
turtle.goto((x,y))
turtle.write(PI*r*r)
turtle.done()