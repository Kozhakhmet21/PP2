def f(a):
    def g(b):
        #nonlocal kerek, global peremenamen shataspau ushyn.
        c=a*b
        return c
    return g

func=f(7)
print(func(6))