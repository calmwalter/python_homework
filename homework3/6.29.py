def isValid(number):
    if getSize(number) < 13 or getSize(number) > 16:
        return False
    match = False
    if prefixMatched(number, 4) or prefixMatched(number, 5) or prefixMatched(number, 37) or prefixMatched(number, 6):
        match = True
    if match == False:
        return False
    print(sumOfDoubleEvenPlace(number))
    print(sumOfOddplace(number))
    if (sumOfDoubleEvenPlace(number)+sumOfOddplace(number)) % 10 == 0:
        return True
    else:
        return False


def sumOfDoubleEvenPlace(number):
    re = 0
    isEven = False
    while number > 1:
        if isEven:
            re += getDigit(number % 10*2)
            number //= 10
            isEven = False
        else:
            number //= 10
            isEven = True
    return re


def getDigit(number):
    if number < 10:
        return number
    else:
        return number % 10+number//10


def sumOfOddplace(number):
    re = 0
    isOdd = True
    while number > 1:
        if isOdd:
            re += number % 10
            number //= 10
            isOdd = False
        else:
            number //= 10
            isOdd = True
    return re


def prefixMatched(number, d):
    if getPrefix(number, getSize(d)) == d:
        return True
    else:
        return False


def getSize(d):
    num = 0
    while d > 0:
        num += 1
        d //= 10
    return num


def getPrefix(number, k):
    n = getSize(number)
    if n < k:
        return number
    else:
        return number//10**(n-k)


number = eval(input("Please enter a credit number:"))

if isValid(number):
    print("It's a valid credit card number.")
else:
    print("It's not a valid credit card number.")
