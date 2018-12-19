import csv
#initialize the csv file
datas = [['name', 'age'],
         ['Bob', 14],
         ['Tom', 23],
        ['Jerry', '18']]

with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in datas:
        writer.writerow(row)
#problem 1
#import the csv file to the lst(problem 1)  
lst=[]
with open("file.csv",'r') as csvfile:
    reader=csv.reader(csvfile)
    lst=list(reader)
print(lst)
print()

#problem 2
#read the file line by line and print it
with open("file.csv",'r') as csvfile:
    reader=csv.reader(csvfile)
    for line in reader:
        print(line)
print()
#problem 3
#write one dimensional data to the file
data=[0,1,2,3,4,5,6,7,8,9]
with open("file1.csv",'w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(data)
print("write 0,1,2,3,4,5,6,7,8,9 to file1.csv sucessfully!")
