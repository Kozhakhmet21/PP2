import re
a=int(input())
while a>0:
    b=str(input())
    x=re.search(r"(?P<mail>(\b[a-z]+).*(<(.*)@gmail.c>|@gmail.com|@gmail.co)+)+",b)
    print(x.group("mail"))
    a-=1

"""
vineet <vineet.iitg@gmail.com>
vineet <vineet.iitg@gmail.co>
vineet <vineet.iitg@gmail.c>

"""