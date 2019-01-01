months=[31,28,31,30,31,30,31,31,30,31,30,31]

names=["January","Febuary","March","April","May","June","July","August","September","October","November","December"]
names1=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
year=eval(input("Enter the year:"))
day=eval(input("Enter thr day of Jan.1 for that year(week):"))
m=1
day-=1
if day==7:
    day=0
for x in names:
    print(" "*5,x," ",year)
    print("-"*30)
    for i in names1:
        print("%-4s"%i,end="")
    print()
    for i in range(day):
        print(" "*4,end="")
    for i in range(months[m-1]):
        print("%-4d"%(i+1),end="")
        if (i+day)%7==6:
            print()
    if (m==2) and ((year%4==0 and year%100) or year%400==0):
        print("%-4d"%29,end="")
        if (29+day)%7==6:
            print()
        day=(day+months[m-1]+1)%7
        
    else:
        day=(day+months[m-1])%7
    m+=1
    print("\n\n")

