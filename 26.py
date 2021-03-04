def f():
    i=0
    while True:
        yield i
        i+=1
        if i>10:
            raise StopIteration

a=f()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))