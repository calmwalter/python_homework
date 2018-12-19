import turtle
import math
pos1=eval(input("Enter p1:"))
pos2=eval(input("Enter p2:"))
pos3=eval(input("Enter p3:"))
def len(pos1,pos2):
    x=((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)**0.5
    return x
l1=len(pos1,pos3)
l2=len(pos1,pos2)
l3=len(pos2,pos3)
PI=3.1415926535
def angle(a,b,c):
    m=(a*a+b*b-c*c)/(2*a*b)
    x=math.acos(m)*180/PI
    return x
a1=angle(l2,l3,l1)
a2=angle(l1,l3,l2)
a3=angle(l2,l1,l3)
turtle.penup()
turtle.goto(pos1)
turtle.write("p1 "+"%.2f"%a1)
turtle.pendown()
turtle.goto(pos2)
turtle.write("p2 "+"%.2f"%a2)
turtle.goto(pos3)
turtle.write("p3 "+"%.2f"%a3)
turtle.goto(pos1)
turtle.hideturtle()

turtle.done()