a=b=[int(x) for x in input().split()]
for i in range(0,len(a)-1):
    if a[i]==a[i+1]:
        print("NO")
    else:
        print("YES")