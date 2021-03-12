a=[str(i) for i in input().split()]
b=[]
for i in range(len(a)):
    b.append(a[len(a)-1-i])
c=''.join(str(i) for i in b)
print(c)