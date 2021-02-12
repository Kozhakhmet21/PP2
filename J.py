a=list(input().split())
b=input()
c=0
for x in range(len(a)):
    d=int(a[x])
    if d > b:
        c+=1

print(c)