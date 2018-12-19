from tkinter import *

window=Tk()
canvas=Canvas(window,width=400,height=400)
canvas.pack()
canvas.create_arc(10,10,390,390,start=0,extent=360*0.2,fill="red",tags="Project")
canvas.create_arc(10,10,390,390,start=360*0.2,extent=360*0.1,fill="blue",tags="Quizzes")
canvas.create_arc(10,10,390,390,start=360*0.3,extent=360*0.3,fill="green",tags="Midterm")
canvas.create_arc(10,10,390,390,start=360*0.6,extent=360*0.4,fill="yellow",tags="Final")
canvas.create_text(300,160,text="Project--20%")
canvas.create_text(200,40,text="Quizzes--10%")
canvas.create_text(80,190,text="Midterm--30%")
canvas.create_text(200,300,text="Final--40%")

window.mainloop()