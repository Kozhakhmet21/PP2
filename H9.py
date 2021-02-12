a=list(input().split())
b=1000
for x in range(len(a)):
    c=int(a[x])
    if c<b and c>0:
        b=c
print(b)