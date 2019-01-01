import time
import turtle
turtle.pensize(4)
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthname = ["Jan.", "Feb.", "Mar.", "Apr.", "May.",
             "Jun.", "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
currentTime = time.time()

totalSeconds = int(currentTime)

currentSecond = totalSeconds % 60

totalMinutes = totalSeconds//60

currentMinute = totalMinutes % 60

totalHours = totalMinutes//60

currentHour = totalHours % 24

totalDays = totalHours//24


def isleapYear(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def getYearMonthDay(days):
    year = 1969
    while days > 0:
        year += 1
        if isleapYear(year):
            days -= 366
        else:
            days -= 365
    if isleapYear(year):
        days += 366
    else:
        days += 365
    month = 0
    while days > 0:
        month += 1
        if month == 2:
            if isleapYear(year):
                days -= 29
            else:
                days -= 28
        else:
            days -= months[month-1]
    if month == 2:
        if isleapYear(year):
            days += 29
        else:
            days += 28
    else:
        days += months[month-1]
    return year, month, days


def draw_number(number, x, y, length):
    
    if number == 0 or number == 2 or number == 3 or number == 5 or number == 6 or number == 7 or number == 8 or number == 9:
        turtle.penup()
        turtle.setheading(0)
        turtle.goto((x, y))
        turtle.pendown()
        turtle.forward(length)
    if number == 2 or number == 3 or number == 4 or number == 5 or number == 6 or number == 8 or number == 9:
        turtle.penup()
        turtle.setheading(0)
        turtle.goto((x, y-length))
        turtle.pendown()
        turtle.forward(length)
    if number == 2 or number == 3 or number == 5 or number == 6 or number == 8 or number == 0 or number == 9:
        turtle.penup()
        turtle.setheading(0)
        turtle.goto((x, y-length*2))
        turtle.pendown()
        turtle.forward(length)
    if number == 4 or number == 5 or number == 6 or number == 8 or number == 9 or number == 0:
        turtle.penup()
        turtle.setheading(0)
        turtle.right(90)
        turtle.goto((x, y))
        turtle.pendown()
        turtle.forward(length)
    if number == 0 or number == 2 or number == 6 or number == 8:
        turtle.penup()
        turtle.setheading(0)
        turtle.right(90)
        turtle.goto((x, y-length))
        turtle.pendown()
        turtle.forward(length)
    if number == 0 or number == 1 or number == 2 or number == 3 or number == 4 or number == 7 or number == 8 or number == 9:
        turtle.penup()
        turtle.setheading(0)
        turtle.right(90)
        turtle.goto((x+length, y))
        turtle.pendown()
        turtle.forward(length)
    if number == 0 or number == 1 or number == 3 or number == 4 or number == 5 or number == 6 or number == 7 or number == 9 or number == 8:
        turtle.penup()
        turtle.setheading(0)
        turtle.right(90)
        turtle.goto((x+length, y-length))
        turtle.pendown()
        turtle.forward(length)


def drawTime(year, month, day):
    x = -100
    y = 30
    turtle.pencolor("red")
    turtle.penup()
    turtle.goto((-50,0))
    turtle.write("年",font=('Arial', 20, 'normal'))
    while year >= 1:
        draw_number(year % 10, x, y, 30)
        year //= 10
        x -= 50
    x=50
    turtle.pencolor("green")
    turtle.penup()
    turtle.goto((100,0))
    turtle.write("月",font=('Arial', 20, 'normal'))
    cnt=0
    while month >= 1:
        draw_number(month % 10, x, y, 30)
        month //= 10
        x -= 50
        cnt+=1
    if cnt<=1:
        draw_number(0,x,y,30)
    cnt=0
    x=200
    turtle.pencolor("blue")
    turtle.penup()
    turtle.goto((250,0))
    turtle.write("日",font=('Arial', 20, 'normal'))
    while day >= 1:
        draw_number(day % 10, x, y, 30)
        day //= 10
        x -= 50
        cnt+=1
    if cnt<=1:
        draw_number(0,x,y,30)
turtle.speed(30)
year, month, day = getYearMonthDay(totalDays)
day+=1
print(year,day,month)
drawTime(year, month, day)
turtle.hideturtle()
turtle.done()