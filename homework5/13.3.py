fileName = input("Enter a filename: ")
openfile=open(fileName,"r")
content=openfile.read()
openfile.close()

#handle the data in content
a=content.split()
l=len(a)
cnt=0
for i in a:
    cnt+=int(i)
print("There are %d scores"%cnt)
print("The total is %d"%cnt) 
print("The average is %.2f"%(cnt/l))
