import random


def shuffle(lst):
    x = random.randint(0, len(lst)-1)
    return lst[x]


lst = input()
m = shuffle(lst)
print(m)
