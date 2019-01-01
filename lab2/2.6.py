# use a dictionary to store the pairs of states and capitals
import random
# import city and capital in file
fp = open("data.txt", "r")
x = []
x = fp.read().split("\n")
y = {}
z = []
for m in x:
    s = []
    s = m.split()
    ci = s[0]
    ca = s[1]
    y[ci] = ca
    z.append(ci)

while True:
    n = random.randint(1, len(z))
    capital = input("What is the capital of %s ? "%(z[n-1]))
    if capital == y[z[n-1]]:
        print("Your answer is correct")
    else:
        print("The correct answer should be ", y[z[n-1]])
