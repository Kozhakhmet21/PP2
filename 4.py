import csv
with open('emp.csv') as a:
    b=csv.reader(a,delimiter=',')
    for row in b:
        print(row)