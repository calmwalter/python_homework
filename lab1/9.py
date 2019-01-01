import time
x=0
while x <= 100:
    print("[",">"*x,"-"*(100-x),"]","%.2f"%x,"%",end="\r")
    time.sleep(0.1)
    x=x+1