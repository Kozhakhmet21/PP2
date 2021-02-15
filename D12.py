a=[int(x) for x in input().split()]
b=0
for i in range(0,len(a)):
    for j in range(len(a)+1):
        if a[i]*-1==b[j]:
            print(i,j)
        else:
            continue