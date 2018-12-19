import time
x=eval(input("Enter thr time zone offset to GMT: "))
totalseconds=int(time.time())
currentseconds=totalseconds%60
totalminutes=totalseconds//60
currentminutes=totalminutes%60
totalhours=totalminutes//60
currenthours=totalhours%24

hour=currenthours+x
if hour>=24:
    hour=hour-24
elif hour<0:
    hour = 24 + hour
print("The current time is ",hour,":",currentminutes,":",currentseconds)