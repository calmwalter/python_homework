x=input("Enter the list1 (separated by space): ")
y=input("Enter the list2 (separated by space): ")
List1=x.split()
List2=y.split()

def MergeList(L1,L2):
    L3=[]
    i,j=0,0
    while i<len(L1) and j<len(L2):
        if L1[i]<L2[j]:
            L3.append(L1[i])
            i+=1
        else:
            L3.append(L2[j])
            j+=1
    L3+=L1[i:]
    L3+=L2[j:]
    return L3

List3=MergeList(List1,List2)
print(List3)
