def f(n):
    a,b=0,1
    for _ in range(0,n):
        yield a+b
        a,b=b,a+b
a=f(10)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))