#this file is used to fomat json file to csv file


#importcsv module
import csv
import json

#read the json file as dictionary
jsonfile=json.load(open("jsonfile.json",'r'))

#write jsonfile to csv file
with open("file2.csv",'w') as csvfile:
    writer=csv.writer(csvfile)
    for key,value in jsonfile.items():
        writer.writerow([key,value])

