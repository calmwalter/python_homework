month=eval(input("month:"))
year=eval(input("year:"))
months=[31,28,31,30,31,30,31,31,30,31,30,31]
if month!=2:
    print(months[month-1])
elif (year%4==0 and year%100) or year%400==0:
    print(29)
else:
    print(28)

