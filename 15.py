def fun(a,b):
    arg1=a+b
    arg2=a/b
    arg3=a*b
    return arg1,arg2,arg3
a,b,c=fun(4,7)
print(a,b,c)
print(fun(4,7)[2])