import random
word=[]
for x in range(65,91):
    word.append(chr(x))
for x in range(48,58):
    word.append(chr(x))
for x in range(97,123):
    word.append(chr(x))

for i in range(10):
    passwd=[]
    for j in range (10):
        passwd.append(word[random.randint(0,61)])
    print("Password ",i+1,end=": ")
    for w in passwd:
        print(w,end="")
    print()