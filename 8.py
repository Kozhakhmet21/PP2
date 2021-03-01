import re
a=int(input())
b=[]
while a>0:
    c=str(input())
    x=re.findall(r"\d+",c)
    b.append(c)
    a-=1
x=0
for x in range(len(b)):
    d=str(b[x])
    y=re.search(r"\b[789]+\d{9}$",d)
    if y:
        print("YES")
    else:
        print('NO')