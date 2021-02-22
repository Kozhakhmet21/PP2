a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
c=d=0
for x in range(0,len(a)-1):
    if a[x]<a[x+1]:
        c+=1
for x in range(0,len(b)-1):
    if b[x]-b[x+1]:
        d+=1
print(c+1,d+1)