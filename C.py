a=int(input())
b=[int(x) for x in input().split()]
c=set()
if len(b)==a:
    for x in range(0,len(b)):
        c.add(b[x])
if len(c)==len(b):
    print("YES")
else:
    print("NO")