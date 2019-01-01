str=input().split()
for x in range(len(str)-1):
    if str[x]!=str[x+1]:
        print(str[x],end=" ")
print(str[len(str)-1])
