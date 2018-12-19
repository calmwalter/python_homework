import re
str=input()
m=re.compile("[1-9][0-9]{10}")
for x in m.findall(str):
    print(x)
