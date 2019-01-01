from GeometricObject import GeometricObject

class Triangle(GeometricObject):
    def __init__(self,side1=1.0,side2=1.0,side3=1.0,color="green",filled=True):
        super().__init__(color,filled)
        self.side1=side1
        self.side2=side2
        self.side3=side3
        if self.side1+self.side2<self.side3 or self.side1+self.side3<self.side2 or self.side2+self.side3<self.side1:
            raise RuntimeError("three given sides cannot form a triangle")
    def getSide1(self):
        return self.side1
    def getSide2(self):
        return self.side2
    def getSide3(self):
        return self.side3
    def setSide1(self,side):
        self.side1=side
        if self.side1+self.side2<self.side3 or self.side1+self.side3<self.side2 or self.side2+self.side3<self.side1:
            raise RuntimeError("three given sides cannot form a triangle")
    def setSide2(self,side):
        self.side2=side
        if self.side1+self.side2<self.side3 or self.side1+self.side3<self.side2 or self.side2+self.side3<self.side1:
            raise RuntimeError("three given sides cannot form a triangle")
    def setSide3(self,side):
        self.side3=side
        if self.side1+self.side2<self.side3 or self.side1+self.side3<self.side2 or self.side2+self.side3<self.side1:
            raise RuntimeError("three given sides cannot form a triangle")       
    def getArea(self):
        s=(self.side1+self.side2+self.side3)/2
        return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5
    def getPerimeter(self):
        return self.side1+self.side2+self.side3
    def __str__(self):
        return "Triangle: side1="+str(self.side1)+" side2= "+str(self.side2)+" side3 = "+str(self.side3)
    
