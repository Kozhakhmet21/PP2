def func():
    a=input()
    b=a%2
    c=a**2
    d=a/2
    print(b,c,d)
print(func.__code__.co_nlocals)