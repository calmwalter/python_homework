import turtle
# 0上1下2左3右 4is not



def drawConncetLine(degree, x, y, direction, length):
    if degree != 0:
        return
    turtle.penup()
    turtle.goto((x, y))
    turtle.setheading(0)
    turtle.pendown()
    if direction == 0:
        turtle.left(90)
        turtle.forward(length)
    elif direction == 1:
        turtle.right(90)
        turtle.forward(length)
    elif direction == 2:
        turtle.left(180)
        turtle.forward(length)
    elif direction == 3:
        turtle.forward(length)


def drawSquare(x1, y1, x2, y2, direction, length):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto((x1, y1))
    if direction == 0:
        turtle.right(90)
        turtle.pendown()
        turtle.forward(length)
        if x1 < x2:
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(length)

        else:
            turtle.right(90)
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(length)

    elif direction == 1:
        turtle.left(90)
        turtle.pendown()
        turtle.forward(length)
        if x1 < x2:
            turtle.right(90)
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(length)

        else:
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(length)

    elif direction == 2:
        turtle.pendown()
        turtle.forward(length)
        if y1 > y2:
            turtle.right(90)
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(length)

        else:
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(length)

    elif direction == 3:
        turtle.left(180)
        turtle.pendown()
        turtle.forward(length)
        if y1 < y2:
            turtle.right(90)
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(length)

        else:
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(length)


def drawHilbertCurve(x1, y1, x2, y2, degree, direction, length, connect):

    l = length/4
    if degree == 0:
        drawSquare(x1, y1, x2, y2, direction, length)
    else:
        # 0->左上上右 1->
        if direction == 0:
            if x1 < x2:
                drawHilbertCurve(x1-l, y1+l, x1-l, y1-l,
                                 degree-1, 2, length/2, 1)
                drawConncetLine(degree-1, x1-l, y1-l, 1, length/2)

                drawHilbertCurve(x1-l, y1-length+l, x1+l, y1 -
                                 length+l, degree-1, direction, length/2, 3)
                drawConncetLine(degree-1, x1+l, y1 - length+l, 3, length/2)

                drawHilbertCurve(x2-l, y2-length+l, x2+l, y2 -
                                 length+l, degree-1, direction, length/2, 0)
                drawConncetLine(degree-1, x2+l, y2-length+l, 0, length/2)

                drawHilbertCurve(x2+l, y2-l, x2+l, y2+l,
                                 degree-1, 3, length/2, connect)
                drawConncetLine(degree-1, x2+l, y2+l, connect, length/2)
            else:
                drawHilbertCurve(x1+l, y1+l, x1+l, y1-l,
                                 degree-1, 3, length/2, 1)
                drawConncetLine(degree-1, x1+l, y1-l, 1, length/2)

                drawHilbertCurve(x1+l, y1-length+l, x1-l, y1 -
                                 length+l, degree-1, direction, length/2, 2)
                drawConncetLine(degree-1, x1-l, y1-length+l, 2, length/2)

                drawHilbertCurve(x2+l, y2-length+l, x2-l, y2 -
                                 length+l, degree-1, direction, length/2, 0)
                drawConncetLine(degree-1, x2-l, y2-length+l, 0, length/2)

                drawHilbertCurve(x2-l, y2-l, x2-l, y2+l,
                                 degree-1, 2, length/2, connect)
                drawConncetLine(degree-1, x2-l, y2+l, connect, length/2)
        elif direction == 2:
            if y1 > y2:
                drawHilbertCurve(x1-l, y1+l, x1+l, y1+l,
                                 degree-1, 0, length/2, 3)
                drawConncetLine(degree-1, x1+l, y1+l, 3, length/2)

                drawHilbertCurve(x1+length-l, y1+l, x1+length-l,
                                 y1-l, degree-1, direction, length/2, 1)
                drawConncetLine(degree-1, x1+length-l, y1-l, 1, length/2)

                drawHilbertCurve(x2+length-l, y2+l, x2+length-l,
                                 y2-l, degree-1, direction, length/2, 2)
                drawConncetLine(degree-1, x2+length-l, y2-l, 2, length/2)

                drawHilbertCurve(x2+l, y2-l, x2-l, y2-l,
                                 degree-1, 1, length/2, connect)
                drawConncetLine(degree-1, x2-l, y2-l, connect, length/2)
            else:
                drawHilbertCurve(x1-l, y1-l, x1+l, y1-l,
                                 degree-1, 1, length/2, 3)
                drawConncetLine(degree-1, x1+l, y1-l, 3, length/2)

                drawHilbertCurve(x1+length-l, y1-l, x1+length-l,
                                 y1+l, degree-1, direction, length/2, 0)
                drawConncetLine(degree-1, x1+length-l, y1+l, 0, length/2)

                drawHilbertCurve(x2+length-l, y2-l, x2+length-l,
                                 y2+l, degree-1, direction, length/2, 2)
                drawConncetLine(degree-1, x2+length-l, y2+l, 2, length/2)

                drawHilbertCurve(x2+l, y2+l, x2-l, y2+l,
                                 degree-1, 0, length/2, connect)
                drawConncetLine(degree-1, x2-l, y2+l, connect, length/2)
        elif direction == 1:
            if x1 < x2:
                drawHilbertCurve(x1-l, y1-l, x1-l, y1+l,
                                 degree-1, 2, length/2, 0)
                drawConncetLine(degree-1, x1-l, y1+l, 0, length/2)

                drawHilbertCurve(x1-l, y1+length-l, x1+l, y1 +
                                 length-l, degree-1, direction, length/2, 3)
                drawConncetLine(degree-1, x1+l, y1+length-l, 3, length/2)

                drawHilbertCurve(x2-l, y2+length-l, x2+l, y2 +
                                 length-l, degree-1, direction, length/2, 1)
                drawConncetLine(degree-1, x2+l, y2+length-l, 1, length/2)

                drawHilbertCurve(x2+l, y2+l, x2+l, y2-l,
                                 degree-1, 3, length/2, connect)
                drawConncetLine(degree-1, x2+l, y2-l, connect, length/2)
            else:
                drawHilbertCurve(x1+l, y1-l, x1+l, y1+l,
                                 degree-1, 3, length/2, 0)
                drawConncetLine(degree-1, x1+l, y1+l, 0, length/2)

                drawHilbertCurve(x1+l, y1+length-l, x1-l, y1 +
                                 length-l, degree-1, direction, length/2, 2)
                drawConncetLine(degree-1, x1-l, y2-l+length, 2, length/2)

                drawHilbertCurve(x2+l, y2+length-l, x2-l, y2 +
                                 length-l, degree-1, direction, length/2, 1)
                drawConncetLine(degree-1, x2-l, y2-l+length, 1, length/2)

                drawHilbertCurve(x2-l, y2+l, x2-l, y2-l,
                                 degree-1, 2, length/2, connect)
                drawConncetLine(degree-1, x2-l, y2-l, connect, length/2)
        elif direction == 3:
            if y1 > y2:
                drawHilbertCurve(x1+l, y1+l, x1-l, y1+l,
                                 degree-1, 0, length/2, 2)
                drawConncetLine(degree-1, x1-l, y1+l, 2, length/2)

                drawHilbertCurve(x1-length+l, y1+l, x1-length+l,
                                 y1-l, degree-1, direction, length/2, 1)
                drawConncetLine(degree-1, x1-length+l, y1-l, 1, length/2)

                drawHilbertCurve(x2-length+l, y2+l, x2-length+l,
                                 y2-l, degree-1, direction, length/2, 3)
                drawConncetLine(degree-1, x2-length+l, y2-l, 3, length/2)

                drawHilbertCurve(x2-l, y2-l, x2+l, y2-l,
                                 degree-1, 1, length/2, connect)
                drawConncetLine(degree-1, x2+l, y2-l, connect, length/2)
            else:
                drawHilbertCurve(x1+l, y1-l, x1-l, y1-l,
                                 degree-1, 1, length/2, 2)
                drawConncetLine(degree-1, x1-l, y1-l, 2, length/2)

                drawHilbertCurve(x1-length+l, y1-l, x1-length+l,
                                 y1+l, degree-1, direction, length/2, 0)
                drawConncetLine(degree-1, x1-length+l, y1+l, 0, length/2)

                drawHilbertCurve(x2-length+l, y2-l, x2-length+l,
                                 y2+l, degree-1, direction, length/2, 3)
                drawConncetLine(degree-1, x2-length+l, y2+l, 3, length/2)

                drawHilbertCurve(x2-l, y2+l, x2+l, y2+l,
                                 degree-1, 0, length/2, connect)
                drawConncetLine(degree-1, x2+l, y2+l, connect, length/2)


degree = eval(input("Enter the order of the Hilbert curve:"))
turtle.speed(100)
drawHilbertCurve(-100, 100, 100, 100, degree, 0, 200, 4)
turtle.done()
