import csv
with open('emp.csv') as a:
    b=csv.reader(a,delimiter=',')
    for row in b:
        print(row[0],row[1])

#Yagyni soldan onga qarai emes jogarydan tomenge dict. retynde shygady.