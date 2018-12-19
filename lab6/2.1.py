#this file used to output the dataset
import random

#the rank
rank=["assistant","associate","full"]

#open file
datafile=open("data.txt",'w')

#output 1000 times
for i in range(1000):
    rankName=rank[random.randint(0,2)]
    salary=0.0
    if rankName==rank[0]:
        salary=random.random()*30000+50000
    elif rankName==rank[1]:
        salary=random.random()*50000+60000
    else:
        salary=random.random()*55000+75000
    datafile.write("FirstName%d LastName%d %s %.2f\n"%(i+1,i+1,rankName,salary))

datafile.close()
print("sucessfully write to file!")

