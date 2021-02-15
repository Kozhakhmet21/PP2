a=[int(x) for x in input().split()]
b=0
for x in range(0,len(a)):
    if a[x]<a[x+1]:
        b+=1
    else:
        continue
if b<10:
    print("YES")
else:
    print("NO")