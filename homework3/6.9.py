#Converts from feet to meters
def footToMeter(foot):
    return foot*0.305
def meterToFoot(meter):
    return meter/0.305

print("%-10s%-10s%-5s%-10s%-10s\n"%("Feet","Meters","|","Meters","Feet"))
for i in range(1,11):
    meter=0
    if i%2==1:
        meter=20+(i-1)//2*10
    else:
        meter=20+(i-1)//2*10+6
    print("%-10.1f%-10.3f%-5s%-10.1f%-10.3f"%(i,footToMeter(i),"|",meter,meterToFoot(meter)))