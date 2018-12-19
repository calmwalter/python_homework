def multiplyMatrix(a,b):
    n=len(a)
    c=[[0]*n for row in range(n)]
    for i in range (0,n):
        for k in range (0,n):
            for j in range (0,n):
                c[i][j]=c[i][j]+a[i][k]*b[k][j]
    return c

a=eval(input())
b=eval(input())
c=multiplyMatrix(a,b)
print(c)