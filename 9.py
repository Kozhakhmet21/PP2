import re
a=int(input())
while a>0:
    b=str(input())
    x=re.search(r"(?P<mail>.*(<(\b[a-z]+)@(\b[a-z]+).com>)+)+",b)
    y=re.search(r"(?P<mmail>(\b[a-z]+).*(<(.*)@gmail.c>|@gmail.com|@gmail.co)+)+",b)
    z=re.search(r"^[a-zA-Z][\w\-\.]*@[A-Za-z]+\.[a-zA-Z]{1,3}$",b)
    if x:
        print(x.group("mail"))
    elif y:
        print(y.group("mail"))
    elif z:
        print(z.group("mail"))
    a-=1