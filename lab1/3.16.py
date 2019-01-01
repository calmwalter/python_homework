import turtle
turtle.penup()

def draw_graph(pos,color,edge):
    turtle.goto(pos)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    turtle.circle(50,steps=edge)
    turtle.end_fill()
    turtle.penup()

turtle.right(60)
draw_graph((-400,0),"red",3)
turtle.left(15)
draw_graph((-200,0),"green",4)
turtle.left(9)
draw_graph((0,0),"yellow",5)
turtle.left(6)
draw_graph((200,0),"black",6)
turtle.left(7.5)
draw_graph((400,0),"blue",8)
turtle.hideturtle()
turtle.done()