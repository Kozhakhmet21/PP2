a=[int(i) for i in input().split()]
x=1
for i in range(len(a)):
    x*=a[i]
print(x)