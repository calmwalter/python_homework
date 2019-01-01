import time
t=input("Enter the number of second :")
time.sleep(1)
t=t-1
while t>1:
    print("%d seconds remaining"%t
    time.sleep(1)
    t-=1
if t>0:
    print("1 second remianing")
    time.sleep(1)
print("Stopped")
