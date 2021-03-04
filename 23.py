def f():
    yield 1
    yield 2
    yield 3
    yield 4
a=f()
print(next(a))
print(next(a))
print(next(a))