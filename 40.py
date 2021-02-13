def f(a):
    for x in range(len(a)):
        if a[x]%15==0:
            print(a[x])

f([14,15,18,30,45,67,90,87])