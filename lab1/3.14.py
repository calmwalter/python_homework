import turtle
turtle.penup()
turtle.pensize(10)

def write_circle(pos, color):
    turtle.goto(pos)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(50)
    turtle.penup()

write_circle((-120, -50), "blue")
write_circle((0, -50), "black")
write_circle((120, -50), "red")
write_circle((-60, -100), "yellow")
write_circle((60, -100), "green")
turtle.done()
