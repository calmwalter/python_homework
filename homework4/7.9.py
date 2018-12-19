class LinearEquation:
    def __init__(self,a,b,e,c,d,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c
    def getD(self):
        return self.__d
    def getE(self):
        return self.__e
    def getF(self):
        return self.__f
    def  isSolvable(self):
        if self.__a*self.__d-self.__b*self.__c==0:
            return False
        else:
            return True
    def getX(self):
        if self.isSolvable()==False:
            return
        return (self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
    def getY(self):
        if self.isSolvable()==False:
            return 
        return (self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c) 
x1,y1,x2,y2=eval(input("Enter the endpoint of the first line segment:"))
x3,y3,x4,y4=eval(input("Enter the endpoint of the second line segment:"))

a=y2-y1
b=x1-x2
c=x1*y2-y1*x2
d=y4-y3
e=x3-x4
f=x3*y4-y3*x4
le=LinearEquation(a,b,c,d,e,f)
print("The intersecting point is: (%.1f, %.1f)"%(le.getX(),le.getY()))