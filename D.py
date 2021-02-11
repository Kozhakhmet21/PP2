a=input()
b=[int(a) for a in a.split()]
for x in range(0,len(a)):
    if b[x]>b[x+1]:
        print(b[x])