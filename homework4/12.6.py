from tkinter import *
PI = 3.1415926535


class Circle2D:
    def __init__(self, x=0, y=0, radius=0):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getArea(self):
        return PI*self.getRadius()**2

    def getPerimeter(self):
        return 2*PI*self.getRadius()

    def containsPoint(self, x, y):
        if ((x-self.getX())**2+(y-self.getY())**2)**0.5 < self.getRadius():
            return True
        else:
            return False

    def contains(self, circle2D):
        if ((circle2D.getX()-self.getX())**2+(circle2D.getY()-self.getY())**2)**0.5 < abs(self.getRadius()-circle2D.getRadius()):
            return True
        else:
            return False

    def overlaps(self, circle2D):
        if ((circle2D.getX()-self.getX())**2+(circle2D.getY()-self.getY())**2)**0.5 < abs(self.getRadius()+circle2D.getRadius()) and ((circle2D.getX()-self.getX())**2+(circle2D.getY()-self.getY())**2)**0.5 > abs(self.getRadius()-circle2D.getRadius()):
            return True
        else:
            return False


class circleDisplay:
    def __init__(self):
        window = Tk()
        window.title("Circle2D")
        self.width = 500
        self.height = 300
        self.c1 = Circle2D(self.width/3, self.height/3, 50)
        self.c2 = Circle2D(self.width/3+50, self.height/3+50, 80)
        self.canvas = Canvas(window, width=self.width, height=self.height)
        self.canvas.pack(side=LEFT)
        self.canvas.create_oval(self.c1.getX()-self.c1.getRadius(), self.c1.getY(
        )-self.c1.getRadius(), self.c1.getX()+self.c1.getRadius(), self.c1.getY()+self.c1.getRadius(), tags="c1")
        self.canvas.create_oval(self.c2.getX()-self.c2.getRadius(), self.c2.getY(
        )-self.c2.getRadius(), self.c2.getX()+self.c2.getRadius(), self.c2.getY()+self.c2.getRadius(), tags="c2")
        self.canvas.create_text(
            240, 20, text="Two circle don't intersect", tags="text")
        self.canvas.bind("<B1-Motion>", self.moveCircle)
        mainloop()

    def moveCircle(self, event):
        if self.c1.overlaps(self.c2):
            self.canvas.delete("text")
            self.canvas.create_text(
                240, 20, text="Two circles intersect", tags="text")
        else:
            self.canvas.delete("text")
            self.canvas.create_text(
                240, 20, text="Two circles don't intersect", tags="text")
        if self.c1.containsPoint(event.x, event.y):
            self.canvas.delete("c1")
            self.c1.setX(event.x)
            self.c1.setY(event.y)
            self.canvas.create_oval(self.c1.getX()-self.c1.getRadius(), self.c1.getY(
            )-self.c1.getRadius(), self.c1.getX()+self.c1.getRadius(), self.c1.getY()+self.c1.getRadius(), tags="c1")
        elif self.c2.containsPoint(event.x, event.y):
            self.canvas.delete("c2")
            self.c2.setX(event.x)
            self.c2.setY(event.y)
            self.canvas.create_oval(self.c2.getX()-self.c2.getRadius(), self.c2.getY(
            )-self.c2.getRadius(), self.c2.getX()+self.c2.getRadius(), self.c2.getY()+self.c2.getRadius(), tags="c2")


circleDisplay()
