a=[int(b) for b in input().split()]
c=1
for i in range(0,len(a)-1):
    if a[i]!=a[i+1]:
        c+=1
print(c)