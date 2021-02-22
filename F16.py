a=[str(x) for x in input().split()]
b=set()
c=1
for x in a:
    if x in b:
        c+=1
    else:
        b.add(x)
        continue
print(c)