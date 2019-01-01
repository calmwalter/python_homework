#this file is used to format csv file to json

import json
import csv

#read csvfile
dic=[]
with open("file.csv",'r') as csvfile:
    reader=csv.reader(csvfile)
    dic=dict(reader)

#write data to json file
json.dump(dic,open("jsonfile.json",'w'))


#verify the content of 
print(json.load(open("jsonfile.json",'r')))
