import time
x=1
while x <= 100:
    print("%.2f"%x,"%",end="\r")
    time.sleep(0.1)
    x=x+1