import turtle
pos1=eval(input("Enter p1:"))
pos2=eval(input("Enter p2:"))
pos3=eval(input("Enter p3:"))
turtle.penup()
turtle.goto(pos1)
turtle.write("p1"+str(pos1))
turtle.pendown()
turtle.goto(pos2)
turtle.write("p2"+str(pos2))
turtle.goto(pos3)
turtle.write("p3"+str(pos3))
turtle.goto(pos1)
turtle.hideturtle()
def len(pos1,pos2):
    x=((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)**0.5
    return x
l1=len(pos1,pos2)
l2=len(pos1,pos3)
l3=len(pos2,pos3)
s=(l1+l2+l3)/2
area=(s*(s-l1)*(s-l2)*(s-l3))**0.5
turtle.penup()
turtle.goto((pos1[0],pos1[1]-50))
turtle.write("The area of the triangle is"+"%.1f"%area)

turtle.done()