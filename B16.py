a=[int(x) for x in input().split()]
b=[int(k) for k in input().split()]
c=0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            c+=1
        elif a[i]==b[j+1]:
            c+=1
        else:
            continue
print(c)