fileName = input("Enter a filename: ")
rep=input("Enter the string to be removed: ")
#get the content of the file
openfile=open(fileName,"r")
content=openfile.read()
openfile.close()

#delete the content that dont needed
x=content.find(rep)
while x!=-1:
    content=content[:x]+content[31+len(rep):]
    x=content.find(rep)
#write the content to the file
writefile=open(fileName,"w")
writefile.write(content)
writefile.close()
print("Done")