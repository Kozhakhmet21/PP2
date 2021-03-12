def func(a):
    b=[]
    for i in range(0,len(a)):
        if a[i]%2==0:
            b.append(a[i])
    print(b)
a=[int(i) for i in input().split()]
func(a)