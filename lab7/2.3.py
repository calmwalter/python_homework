from tkinter import *
class keyArrow:
    def __init__(self):
        self.x=200
        self.y=200
        self.window = Tk()
        self.window.title("Arrow Key")

        self.canvas=Canvas(self.window,width=400,height=400)
        self.canvas.pack()
        self.canvas.bind("<Key>",self.keyevent)
        self.canvas.focus_set()

        self.window.mainloop()

    def keyevent(self,event):
        print(event.keysym)
        if event.keysym=="Up":
            self.canvas.create_line(self.x,self.y,self.x,self.y-5)
            self.y-=5
        elif event.keysym=="Down":
            self.canvas.create_line(self.x,self.y,self.x,self.y+5)
            self.y+=5
        elif event.keysym=="Left":
            self.canvas.create_line(self.x,self.y,self.x-5,self.y)
            self.x-=5
        elif event.keysym=="Right":
            self.canvas.create_line(self.x,self.y,self.x+5,self.y)
            self.x+=5





keyArrow()


