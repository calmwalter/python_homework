import re
str=input("Enter a genome string: ")

m=re.compile("ATG(.*?)(TAG|TAA|TGA)")
for x in m.findall(str):
    print(x[0])
