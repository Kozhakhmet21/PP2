def f():
    for i in range(0,10):
        yield i
a=f()
for x in a:
    print(x)