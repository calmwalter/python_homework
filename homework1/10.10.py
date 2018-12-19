def reverse(s):
    s1=[]
    l=len(s)-1
    while l >= 0:
        s1.append(s[l])
        l=l-1
    return s1

s=[]
s=input()
m=reverse(s)
for x in m:
    print(x,end="")