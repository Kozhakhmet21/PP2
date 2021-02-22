x=6
def f():
    global x
    x=8
    print(x)
print(x) #mynau byrynshy jasgan son ozgermeidy, 1-shy funcia shaqyru kerek.
f()
print(x)