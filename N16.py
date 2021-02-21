a=input().split()
b=0
for x in range(0,len(a)+1):
    if a[x]==a[x+1]:
        b+=1
    if b>len(a):
        c=a[x]

print(c)