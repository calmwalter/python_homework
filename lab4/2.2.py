def isPalindromicPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    y = []
    while x >= 1:
        y.append(x % 10)
        x //= 10
    print(y)
    l = len(y)
    for i in range(l):
        if y[i] != y[l-i-1]:
            return False
    return True


cnt = 0
x = 101*[0]
number = 2
while cnt <= 100:
    if isPalindromicPrime(number):
        x[cnt] = number
        cnt += 1
    number += 1

for i in range(100):
    print("%-8d" % x[i], end="")
    if (i+1) % 10 == 0:
        print()
