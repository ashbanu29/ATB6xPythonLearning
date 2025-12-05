import csv

with open('tds.csv', 'r') as file:
    reader =  csv.reader(file)
    for column in reader:
        print(column[0],column[1], sep ="|")
