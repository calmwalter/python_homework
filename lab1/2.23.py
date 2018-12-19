import turtle


def draw_circle(r, pos):
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    turtle.circle(r)


r = eval(input("Input the radius: "))
draw_circle(r, (-r, 0))
draw_circle(r, (r, 0))
draw_circle(r, (-r, -2*r))
draw_circle(r, (r, -2*r))
