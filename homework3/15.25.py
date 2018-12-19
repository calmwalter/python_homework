from tkinter import *


class SierpinskiTriangle:
    def __init__(self):
        window = Tk()
        window.title("snow")

        self.width = 200
        self.height = 200
        self.canvas = Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        frame1 = Frame(window)
        frame1.pack()

        Label(frame1, text="Enter an order: ").pack(side=LEFT)
        self.order = StringVar()
        entry = Entry(frame1, textvariable=self.order, justify=RIGHT)
        entry.pack(side=LEFT)
        Button(frame1, text="Display snow",
               command=self.display).pack(side=LEFT)
        window.mainloop()

    def display(self):
        self.canvas.delete("line")

        p1 = [100, 10]
        p2 = [100-(150-10)/3**0.5, 150]
        p3 = [100+(150-10)/3**0.5, 150]
        self.displayKochSnow(int(self.order.get()),p2,p1,1)
        self.displayKochSnow(int(self.order.get()),p1,p3,1)
        self.displayKochSnow(int(self.order.get()),p2,p3,0)

    def drawtwoline(self, p1, p2, cp):
        p4 = self.getp4(p1, p2, cp)
        self.drawLine(p4, p1)
        self.drawLine(p4, p2)

    def getthreetwopos(self, p1, p2):
        temp=p1
        if p1[0]>p2[0]:
            p1=p2
            p2=temp
        dx = abs(p1[0]-p2[0])/3
        minx = min(p1[0], p2[0])
        dy = abs(p1[1]-p2[1])/3
        miny = min(p1[1], p2[1])
        if p1[1]<p2[1]:
            dx = abs(p1[0]-p2[0])/3
            minx = min(p1[0], p2[0])
            dy = abs(p1[1]-p2[1])/3
            miny = min(p1[1], p2[1])
            p3 = [minx+dx, miny+dy]
            p4 = [minx+dx*2, miny+dy*2]
            return p3, p4
        else:
            p3 = [minx+dx, miny+dy*2]
            p4 = [minx+dx*2, miny+dy]
            return p3, p4
    def getcp(self, p1, p2, p3):
        return [(p1[0]+p2[0]+p3[0])/3, (p1[1]+p2[1]+p3[1])/3]

    def getp4(self, p1, p2, cp):
        p12 = self.midpoint(p1, p2)
        p4 = [p12[0]*2-cp[0], p12[1]*2-cp[1]]
        return p4

    #direction 是方向，向上为1，向下为0
    def displayKochSnow(self,order,p1,p2,direction):
        temp=p1
        if p1[0]>p2[0]:
            p1=p2
            p2=temp
        if order==0:
            self.drawLine(p1,p2)
            return
        else:
            c=2*[0]
            a,b=self.getthreetwopos(p1,p2)
            #判断ab位置关系
            if a[1]==b[1]:
                c[0]=(a[0]+b[0])/2
                if direction==1:
                    c[1]=a[1]+(a[0]-b[0])/2*3**0.5
                else:
                    c[1]=a[1]-(a[0]-b[0])/2*3**0.5
                
                self.displayKochSnow(order-1,p1,a,direction)
                self.displayKochSnow(order-1,a,c,direction)
                self.displayKochSnow(order-1,c,b,direction)
                self.displayKochSnow(order-1,b,p2,direction)
            elif a[0]<b[0] and a[1]>b[1]:
                if direction==1:
                    c[0]=b[0]-self.getLength(a,b)
                    c[1]=b[1]
                    self.displayKochSnow(order-1,p1,a,direction)
                    self.displayKochSnow(order-1,a,c,0)
                    self.displayKochSnow(order-1,c,b,direction)
                    self.displayKochSnow(order-1,b,p2,direction)
                else:
                    c[0]=a[0]+self.getLength(a,b)
                    c[1]=a[1]
                    self.displayKochSnow(order-1,p1,a,0)
                    self.displayKochSnow(order-1,a,c,0)
                    self.displayKochSnow(order-1,c,b,1)
                    self.displayKochSnow(order-1,b,p2,0)
                
            else:
                if direction==1:
                    c[0]=a[0]+self.getLength(a,b)
                    c[1]=a[1]
                    self.displayKochSnow(order-1,p1,a,1)
                    self.displayKochSnow(order-1,a,c,1)
                    self.displayKochSnow(order-1,c,b,0)
                    self.displayKochSnow(order-1,b,p2,1)
                else:
                    c[0]=b[0]-self.getLength(a,b)
                    c[1]=b[1]
                    self.displayKochSnow(order-1,p1,a,0)
                    self.displayKochSnow(order-1,a,c,1)
                    self.displayKochSnow(order-1,c,b,0)
                    self.displayKochSnow(order-1,b,p2,0)


    def getLength(self,p1,p2):
        return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
    def drawLine(self, p1, p2):
        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], tags="line")

    def midpoint(self, p1, p2):
        p = 2*[0]
        p[0] = (p1[0]+p2[0])/2
        p[1] = (p1[1] + p2[1])/2
        return p


SierpinskiTriangle()