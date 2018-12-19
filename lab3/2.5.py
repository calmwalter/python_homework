import turtle
turtle.pensize(2)
turtle.color("black")
turtle.penup()
turtle.goto((-240,-240))
turtle.pendown()
turtle.goto((240,-240))
turtle.goto((240,240))
turtle.goto((-240,240))
turtle.goto((-240,-240))
def draw_sq(x,y,z):
    turtle.penup()
    turtle.goto((x,y))
    turtle.begin_fill()
    turtle.pendown()
    turtle.goto((x+z,y))
    turtle.goto((x+z,y+z))
    turtle.goto((x,y+z))
    turtle.goto((x,y))
    turtle.end_fill()

x=-240
y=-240

while y<240:
    while x<240:
        draw_sq(x,y,60)
        x+=120
    y+=120
    x=-240

y=-240
while y<240:
    while x<240:
        draw_sq(x+60,y+60,60)
        x+=120
    y+=120
    x=-240   
turtle.done()
