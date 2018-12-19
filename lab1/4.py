x=1
y=1
while x<=9:
    while y<=x:
        print("%-2d"%y,"* ","%-2d"%x, "= " , "%2d"%(x*y),end=" ")
        y=y+1
    print("")
    y=1
    x=x+1