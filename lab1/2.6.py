x=eval(input("Enter a number between 0 and 1000: "))
sum=0
while x>10:
    sum=sum+x%10
    x=x//10
sum+=x
print("The sum of the digit is ",sum)