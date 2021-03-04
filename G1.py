import re
a=[str(x) for x in input().split()]
b=str(input())
c=str(input())
x=0

for i in range(len(a)):
    x=re.search(b,a[i])
    if x:
        d=''.join(str(x) for x in a )
i=0
for i in range(len(d)):
    if b==d[i]:
        d[i]==c
print(c)