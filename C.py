a=input()
b=[int(a) for a in a.split()]
c=0
for x in b:
    if int(x)>0:
        c+=1

print(c)