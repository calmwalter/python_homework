l = input()
# use list
m = []
for x in range(len(l)):
    j = False
    for i in m:
        if l[x] == i:
            j = True
            break
    if j:
        continue
    for k in range(x+1, len(l)):
        if l[k] == l[x]:
            m.append(l[x])
            break
print(m)

# use set

a = set(l)
b = []
for x in a:
    cnt = 0
    for i in l:
        if i == x:
            cnt = cnt+1
    if cnt > 1:
        b.append(x)

print(b)


# set is better ,because its easier to use