fileName = input("Enter a filename: ")
openfile=open(fileName,"r")
content=openfile.read()
openfile.close()

#handle the data in content
a=content.split()

#the number of the word
l=len(a)
cnt=0
cnt1=1
for i in content:
    cnt+=1
    if i=='\n':
        cnt1+=1

print(cnt,"characters")
print(l,"words")
print(cnt1,"lines")

