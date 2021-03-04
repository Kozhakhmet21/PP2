a=[str(x) for x in input().split()]
b=list()
for x in range(len(a)):
    c=len(a[x])
    b.append(c)
d=max(b)
for x in range(len(a)):
    c=len(a[x])
    if c==d:
        print(a[x])
        print(d)