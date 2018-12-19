from tkinter import *
import time
theta=0
window=Tk()

canvas=Canvas(window,width=400,height=400)
canvas.pack()

while 1:
    theta+=1
    arc1=canvas.create_arc(10,10,390,390,start=theta,extent=30,fill="red")
    arc2=canvas.create_arc(10,10,390,390,start=theta+90,extent=30,fill="red")
    arc3=canvas.create_arc(10,10,390,390,start=theta+180,extent=30,fill="red")
    arc4=canvas.create_arc(10,10,390,390,start=theta+270,extent=30,fill="red")
    canvas.update()
    time.sleep(0.01)
    canvas.delete(arc1)
    canvas.delete(arc2)
    canvas.delete(arc3)
    canvas.delete(arc4)

window.mainloop()

