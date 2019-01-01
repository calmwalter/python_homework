class Location:
    def __init__(self):
        self.row=0
        self.column=0
        self.maxValue=0
    def locateLargest(self,a):
        l=len(a)
        maxval=a[0][0]
        r=0
        c=0
        for x in range(l):
            l1=len(a[x])
            for y in range(l1):
                if a[x][y]>maxval:
                    maxval=a[x][y]
                    r=x
                    c=y
        self.row=r
        self.column=c
        self.maxValue=maxval
        return r,c,maxval

row,colunm=eval(input("Enter the number of rows and colunms in the list:"))
a=[]
for i in range(row):
    print("Enter row %d:"%i,end=" ")
    str = input().split()
    arr=[]
    for n in str:
        arr.append(eval(n))
    a.append(arr)
lc=Location()
r,c,maxval=lc.locateLargest(a)
print("The location of the largset element is %f at (%d,%d)"%(maxval,r,c))
        
        