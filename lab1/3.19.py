import turtle
pos1=eval(input("Enter p1:"))
pos2=eval(input("Enter p2:"))

turtle.penup()
turtle.goto(pos1)
turtle.write("p1 "+str(pos1))
turtle.pendown()
turtle.goto(pos2)
turtle.write("p2 "+str(pos2))
turtle.hideturtle()
turtle.done()