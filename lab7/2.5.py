from tkinter import *
import random


class displayball:
    def __init__(self):
        self.window=Tk()
        self.window.title("Random Balls")
        self.width=600
        self.height=400
        self.canvas=Canvas(self.window,width=self.width,height=self.height)
        self.canvas.pack()
        self.display()

        self.button=Button(self.window,text="display",command=self.deleteball)
        self.button.pack()

        self.window.mainloop()



    def randomcolor(self):
        color=""
        code=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        for i in range(6):
            color+=code[random.randint(0,15)]
        return "#"+color

    def display(self):
        x1,y1=random.randint(0,600),random.randint(0,400)
        self.ball1=self.canvas.create_oval(x1,y1,x1+8,y1+8,fill=self.randomcolor())

        x2,y2=random.randint(0,600),random.randint(0,400)
        self.ball2=self.canvas.create_oval(x2,y2,x2+8,y2+8,fill=self.randomcolor())

        x3,y3=random.randint(0,600),random.randint(0,400)
        self.ball3=self.canvas.create_oval(x3,y3,x3+8,y3+8,fill=self.randomcolor())

        x4,y4=random.randint(0,600),random.randint(0,400)
        self.ball4=self.canvas.create_oval(x4,y4,x4+8,y4+8,fill=self.randomcolor())

        x5,y5=random.randint(0,600),random.randint(0,400)
        self.ball5=self.canvas.create_oval(x5,y5,x5+8,y5+8,fill=self.randomcolor())

        x6,y6=random.randint(0,600),random.randint(0,400)
        self.ball6=self.canvas.create_oval(x6,y6,x6+8,y6+8,fill=self.randomcolor())

        x7,y7=random.randint(0,600),random.randint(0,400)
        self.ball7=self.canvas.create_oval(x7,y7,x7+8,y7+8,fill=self.randomcolor())

        x8,y8=random.randint(0,600),random.randint(0,400)
        self.ball8=self.canvas.create_oval(x8,y8,x8+8,y8+8,fill=self.randomcolor())

        x9,y9=random.randint(0,600),random.randint(0,400)
        self.ball9=self.canvas.create_oval(x9,y9,x9+8,y9+8,fill=self.randomcolor())

        x10,y10=random.randint(0,600),random.randint(0,400)
        self.ball10=self.canvas.create_oval(x10,y10,x10+8,y10+8,fill=self.randomcolor())

    def deleteball(self):
        self.canvas.delete(self.ball1)
        self.canvas.delete(self.ball2)
        self.canvas.delete(self.ball3)
        self.canvas.delete(self.ball4)
        self.canvas.delete(self.ball5)
        self.canvas.delete(self.ball6)
        self.canvas.delete(self.ball7)
        self.canvas.delete(self.ball8)
        self.canvas.delete(self.ball9)
        self.canvas.delete(self.ball10)
        self.display()

displayball()
