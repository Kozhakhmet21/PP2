def func(a):
    i=0
    b=[]
    for i in range(0,len(a)-1):
        if a[i]!=a[i-1]:
            b.append(a[i])
    b.append(a[len(a)-1])
    return b
a=[int(i) for i in input().split()]
b=func(a)
print(b)