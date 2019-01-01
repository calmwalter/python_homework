def isAnagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    s1.sort()
    s2.sort()
    for x in range(len(s1)-1):
        if s1[x] != s2[x]:
            return False
    return True

x=input().split()
y=input().split()

isana=isAnagram(x,y)
if isana:
    print("is an anagram")
else:
    print("is not an anagram")