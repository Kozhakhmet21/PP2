def fun(x):
    return x%2!=0
a=[2,3,4,7,86,45,34,67,4,8,9,11,43]
b=tuple(filter(fun,a))
print(b)
c=list(filter(fun,a))
print(c)