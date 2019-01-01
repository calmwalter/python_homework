import turtle
x1=eval(input("enter the x coordinate:"))
y1=eval(input("enter the y coordinate:"))
width1=eval(input("enter the width of the rectangle:"))
height1=eval(input("enter the height of the rectangle:"))
x2=eval(input("enter the x coordinate:"))
y2=eval(input("enter the y coordinate:"))
width2=eval(input("enter the width of the rectangle:"))
height2=eval(input("enter the height of the rectangle:"))

def drawrec(x,y,width,height):
    turtle.penup()
    turtle.goto((x,y))
    turtle.pendown()
    turtle.goto((x+width,y))
    turtle.goto((x+width,y+height))
    turtle.goto((x,y+height))
    turtle.goto((x,y))
    turtle.penup()
drawrec(x1,y1,width1,height1)
drawrec(x2,y2,width2,height2)
turtle.goto((x1+width1,y1))
turtle.pendown()
if x1<=x2 and y1<=y2 and width1+x1>width2+x2 and height1+y1>height2+y2:
    turtle.write("r2 is inside r1")
elif width1/2+width2/2<abs(x1-x2) and height1/2+height2/2<abs(y1-y2):
    turtle.write("r2 is not overlap r1")
else:
    turtle.write("r2 is overlap r1")
turtle.done()
