import math
def func(a,b):
    i=1
    c=set()
    while a<=i and i<=b:
        c.add(int(math.sqrt(i)))
        i+=1
    print(c)
func(1,30)