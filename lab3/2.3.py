for i in range(8):
    print(" "*(7-i)*4,end="")
    for k in range(i):
        print("%4d"%2**k,end="")
    for k in range(i+1):
        print("%4d"%2**(i-k),end="")
    print()
