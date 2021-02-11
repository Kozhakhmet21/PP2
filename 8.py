def fun(*arg):
    for a in arg:
        print(a,type(a))

fun([1,3,5,7],"hi",5)