pi=0
k=10001
while k<100002:
    for i in range(1,k):
        pi+=(-1)**(i+1)/(2*i-1)
    print(pi*4)
    k+=10000
    pi=0

