fp = open("hamlet.txt", "r")
s = fp.read()
fp.close()
x = set(s)
count = []
for word in x:
    cnt = 0
    for w in s:
        if word == w:
            cnt = cnt+1
    count.append((word, cnt))

count.sort(key=lambda count: count[1],reverse=True)
cnt=0
for x,y in count:
    if x!=' ' and x!='\n':
        print(x,":",y)
        cnt=cnt+1
    if cnt==10:
        break
