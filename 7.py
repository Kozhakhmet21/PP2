def f(a,b,c):
    for i in range(c):
        if a<=c and c<=b:
            i+=1
        else:
            break
    return i
a=[int(i) for i in input().split()]
b=int(input())
c=f(a[0],a[1],b)
if b==c:
    print("YES")
else:
    print("NO")
