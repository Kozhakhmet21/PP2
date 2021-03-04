import re
a=str(input())
b=str(input())
x=re.search(b,a)
if x:
    c=x.span()
    print(c[0])
else:
    print("Not found")