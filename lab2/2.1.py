lst=input().split(" ")
lst1=[]
mean=0
deviation=0
for x in lst:
    lst1.append(eval(x))
    mean=mean+eval(x)
mean=mean/len(lst1)
for x in lst1 :
    deviation=deviation+(x-mean)**2
deviation=(deviation/len(lst1))**0.5

lst1.sort()
l=len(lst1)
print("l:",l)
if l%2==0:
    median=(lst1[len(lst1)//2-1]+lst1[len(lst1)//2])/2
else:
    median=lst1[len(lst1)//2]

print("mean:",mean)
print("deviation:",deviation)
print("median:",median)
