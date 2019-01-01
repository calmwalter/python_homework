import turtle
import math
class RegularPolygon:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n=n
        self.__side=side
        self.__x=x
        self.__y=y
    def getPerimeter(self):
        return self.__side*self.__n
    def getArea(self):
        return (self.__n*self.__side**2)/(4*math.tan(3.1415926535/self.__n))

    
rp=RegularPolygon()
print("Area =",rp.getArea())
print("Perimeter =",rp.getPerimeter())
rp=RegularPolygon(6,4)
print("Area =",rp.getArea())
print("Perimeter =",rp.getPerimeter())
rp=RegularPolygon(10,4,5.6,7.8)
print("Area =",rp.getArea())
print("Perimeter=",rp.getPerimeter())