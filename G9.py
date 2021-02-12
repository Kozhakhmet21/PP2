a=[int(x) for x in input().split()]
b=max(a)
for x in range(0,len(a)):
    if a[x]==b:
        print(a[x],x)