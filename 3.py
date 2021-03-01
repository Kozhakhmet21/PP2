import re
a=str(input())
b=r"\.*\w+"
x=re.findall(b,a)
b=str(x)
d=re.search(r"\w+",b)
e=str(d[0])
i=0
f=[]
for i in range(len(e)-1):
    if e[i]!="_":
        if e[i]==e[i+1]:
            f.append(e[i])
        else:
            continue
if f:
    print(f)
else:
    print(-1)