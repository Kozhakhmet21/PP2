def fun(a):
    return lambda b:b*a
lam=fun(7)
lan=fun(8)
print(lam(4),lan(3))