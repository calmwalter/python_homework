a=input()
b=a.split()
s=[]
for x in b:
    s.append(eval(x))
m=[]
for x in s:
    j=False
    for y in m:
        if x is y:
            j=True
            break
    if j is False:
        m.append(x)
for x in m:
    print(x,end=" ")





