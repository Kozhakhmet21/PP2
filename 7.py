f=open("emp1.csv","r")
line=f.readline() #Ekeuinyn ayrmarshylygy.
lines=f.readlines()
for x in line:
    print(x)
for y in lines:
    print(y)