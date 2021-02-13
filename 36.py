def f(a):
    for x in range(len(a)):
        if a[x]==a[len(a)-1-x]:
            print("yes")
        else:
            print("no")

f("qazaq")