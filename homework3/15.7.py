cnt=0
def main():
    index=eval(input("Enter an index for a Fibonacci number:"))
    print("The Fibonacci number at index",index, "is", fib(index))

def fib(index):
    global cnt
    cnt+=1
    if index==0:
        return 0
    elif index==1:
        return 1
    else:
        return fib(index-1)+fib(index-2)

main()
print(cnt)