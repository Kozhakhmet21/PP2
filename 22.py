def fun(x):
    if x%2!=0:
        return x
a=[5,8,7,45,34,23,80,9,8,88,78,67,77,57]
b=list(map(lambda x:x*2,a))
print(b)
c=list(map(fun,a))
print(c)