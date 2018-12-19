def isValid(side1,side2,side3):
    if side1+side2>side3 and side1+side3>side2 and side2+side3 >side1:
        return True
    else:
        return False

def area(side1,side2,side3):
    p=(side1+side2+side3)/2
    return (p*(p-side1)*(p-side2)*(p-side3))**0.5


x=eval(input("Enter three sides in double:"))
if isValid(x[0],x[1],x[2]):
    s=area(x[0],x[1],x[2])
    print("The area of thr triangle is",s)
else:
    print("Input is invalid")

