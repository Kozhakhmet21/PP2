import re
a=int(input())
while a>0:
    b=str(input())
    x=re.search(r"(?P<mail>.*(<(\b[a-z]+)@(\b[a-z]+).com>)+)+",b)
    if x:
        print(x.group("mail"))
    a-=1