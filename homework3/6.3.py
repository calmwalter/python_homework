#return the reversal of an integer, e.g. reverse(456) returns
#654
def reverse (number):
    re=0
    a=1
    b=0
    while a<number:
        a*=10
        b+=1
    while b >0:
        re+=number%10*10**(b-1)
        number//=10
        b-=1
    return re

#Return true if number is a palindrome
def isPalindrome(number):
    x=reverse(number)
    print(x)
    if x==number:
        print("It's a palindrome.")
    else:
        print("It's not a palindrome.")

x=eval(input("Enter a number:"))
isPalindrome(x)