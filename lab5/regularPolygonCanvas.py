from tkinter import *
import math
class RegularPolygonCanvas(Canvas):
    def __init__(self,numberOfSides,width=200,height=200): 
        super().__init__(width=width,height=height)
        self.width=width
        self.height=height
        self.numberOfSides=numberOfSides
        self.createPolygon()
        self.pack(side=LEFT)
        mainloop()
        
    def createPolygon(self):
        points=[]
        radius=min(self.width/2,self.height/2)
        p=(self.width/2,self.height/2)
       
        for i in range(self.numberOfSides):
            radian=2/self.numberOfSides*math.pi*i
            k=math.tan(radian)
            x1=p[0]-radius/(k*k+1)**0.5
            x2=p[0]+radius/(k*k+1)**0.5
            if 0<=radian and radian<math.pi/2:
                y=p[1]+k*(x1-p[0])
                points.append(x1)
                points.append(y)
            elif 360/self.numberOfSides*i-90<0.001:
                points.append(self.width/2)
                points.append(0)
            elif math.pi>radian and radian>math.pi/2:
                y=p[1]+k*(x2-p[0])
                points.append(x2)
                points.append(y)
            elif math.pi<=radian and radian<math.pi/2*3:
                y=p[1]+k*(x2-p[0])
                points.append(x2)
                points.append(y)
            elif 360/self.numberOfSides*i-270<0.001:
                points.append(self.width/2)
                points.append(self.height)
            elif math.pi*2>radian and radian>math.pi/2*3:
                y=p[1]+k*(x1-p[0])
                points.append(x1)
                points.append(y)                 
        print(points)
        self.create_polygon(points,fill="red")
        
RPC1=RegularPolygonCanvas(3)
RPC2=RegularPolygonCanvas(4)
RPC3=RegularPolygonCanvas(5)
RPC4=RegularPolygonCanvas(6)
RPC5=RegularPolygonCanvas(7)
RPC6=RegularPolygonCanvas(8)



        
