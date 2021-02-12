a=list(input().split())
b=1000
d=0
for x in range(len(a)):
    c=int(x)
    if c!=0:
        if c%2!=0 and c<b:
            b=c
        elif c%2==0:
            continue
    else:
        b=d
print(b)