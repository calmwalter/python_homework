from tkinter import *
from math import *
class CHART:
    def __init__(self,parent,data,width=500,height=400):
        self.win=Canvas(parent,width=width,height=height,bg="white")
        self.__width=width
        self.__height=height
        self.__padding=20
        self.__radius=(min(width,height)-2*self.__padding)/2
        self.raw_data=[x[0] for x in data]
        self.labels=[x[1] for x in data]
        self.colors=[x[2] for x in data]
        self.data=self.calcNomalizedData()
        self.draw()
    def calcNomalizedData(self):
        return [360*x/sum(self.raw_data) for x in self.raw_data]
    def draw(self):
        self.__drawWedges()
        self.__writeLabels()
    def __drawWedges(self):
        self.win.delete('slice')
        cx,cy,r=self.__width/2 ,self.__height/2,self.__radius
        start=0
        for i in range(len(self.data)):
            self.win.create_arc(cx-r,cy-r,cx+r,cy+r,
                            start=start,extent=self.data[i],
                            fill=self.colors[i],tags='slice')
            start+=self.data[i]
    def __writeLabels(self):
        self.win.delete('label')
        cx,cy,r=self.__width/2 ,self.__height/2,self.__radius
        wedge_r=2*r/3
        start=0
        for i in range(len(self.data)):
            x=cy+wedge_r*cos(radians(start+self.data[i]/2))
            y=cy-wedge_r*sin(radians(start+self.data[i]/2))
            self.win.create_text(x,y,text=self.labels[i],
                             font=('Courier',10,'normal'),tags='label')
            start+=self.data[i]
    def setData(self,data):
        self.raw_data=[x[0] for x in data]
        self.labels=[x[1] for x in data]
        self.colors=[x[2] for x in data]
        self.data=self.calcNormalizedData()
def main():
    data1=[[40,"CS","red"],[30,"IS","blue"],[50,"IT","yellow"],]
    data2=[[140,"Freshman","red"],[130,"Sophomore","blue"],[150,"Junior","yellow"],[80,"Senior","green"]]
    win=Tk()
    win.title("Pie Chart")
    chart1=CHART(win,data1)
    chart2=CHART(win,data2)
    chart1.win.pack(side=LEFT)
    chart2.win.pack(side=LEFT)
    win.mainloop()

main()
