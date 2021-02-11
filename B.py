a=input()
b=[int(a) for a in a.split()]
for x in b:
    if int(x)%2==0:
        print(x)