a=[int(x) for x in input().split()]
for i in range(len(a)):
    if i%2!=0 or i==0:
        print(a[i])