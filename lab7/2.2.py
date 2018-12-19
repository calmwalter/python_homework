import time
from datetime import datetime
from tkinter import *
import math
def get_time():
    hour=datetime.now().hour
    minute=datetime.now().minute
    second=datetime.now().second
    return hour,minute,second
hour,minute,second=get_time()

print(hour,minute,second)
window=Tk()
window.title("current time")
canvas=Canvas(window,width=380,height=400)
canvas.pack()
canvas.create_oval(10,10,370,370)
canvas.create_text(20,185,text="9",font= "time 10 bold")
canvas.create_text(185,20,text="12",font= "time 10 bold")
canvas.create_text(185,360,text="6",font= "time 10 bold")
canvas.create_text(360,185,text="3",font= "time 10 bold")
theta1=2*math.pi-math.pi*abs(hour-12)/6-math.pi/6*minute/60-2*math.pi/360*second/60
print(theta1*180/math.pi)
theta2=2*math.pi-math.pi*minute/30-2*math.pi/60*second/60
theta3=2*math.pi-math.pi*second/30
x,y=0,80
def transform(x,y,theta):
    x1=x*math.cos(theta)-y*math.sin(theta)
    y1=x*math.sin(theta)+y*math.cos(theta)
    return x1,y1
x1,y1=transform(x, y, theta1)
x,y=0,110
x2,y2=transform(x,y,theta2)
x,y=0,150
x3,y3=transform(x,y,theta3)

canvas.create_line(185,185,x1+185,185-y1,fill="green")
canvas.create_line(185,185,x2+185,185-y2,fill="blue")
canvas.create_line(185,185,x3+185,185-y3,fill="red")
canvas.create_text(180,385,text="%d:%d:%d"%(hour,minute,second),font = "time 14 bold")

window.mainloop()




