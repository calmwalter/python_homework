import random
x=eval(input("scissor(0), rock(1), paper(2):"))
y=random.randint(0,3)
a=["scissor","rock","paper"]
print("The computer is ",a[y],".You are rock.",end="")

if (x==0 and y==0) or (x==1 and y==1) or (x==2 and y==2):
	print(" It is a draw.")

elif (x==0 and y==1) or (x==1 and y==2) or (x==2 and y==0):
	print(" You loses.")
else:
	print(" You won.")
