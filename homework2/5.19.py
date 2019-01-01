n=eval(input("Enter the number of line:"))
i=0
for i in range(n):
	blank=n-i
	a=i+1
	while blank>0:
		print("   ",end="")
		blank=blank-1
	while a>1:
		print("%-3d"%a,end="")
		a-=1
	while a<=i+1:
		print("%-3d"%a,end="")
		a+=1
	print()

