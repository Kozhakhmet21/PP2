a=[int(b) for b in input().split()]
b=int(input())
c=0
while c<len(a) and a[c]>=b:
    c+=1

print(c+1)