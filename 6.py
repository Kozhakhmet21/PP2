def f(a):
    b=[]
    i=c=1
    while i<=a:
        b.append(i)
        i+=1
    for i in range(len(b)):
        c*=b[i]
    return c
a=int(input())
print(f(a))