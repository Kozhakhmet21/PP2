def fun():
    while a!=0 and b!=0:
        if a>b:
            a%=b
        else:
            b%=a
    return a+b

a=int(input())
b=int(input())
print(fun(a,b))