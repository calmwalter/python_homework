import turtle
def draw_hexagon(pos):
    turtle.penup()
    turtle.goto(pos)
    turtle.left(30)
    turtle.pendown()
    turtle.forward(100)
    x=0
    while x!=5:
        x=x+1
        turtle.left(60)
        turtle.forward(100)
    turtle.left(30)

draw_hexagon((-100,0))
draw_hexagon((100,0))
draw_hexagon((-100,-200))
draw_hexagon((100,-200))
turtle.done()