import re
a=int(input())
b=list()
x=0
while x<a:
    c=str(input())
    b.append(c)
    x+=1
for i in range(0,len(b)):
    d=re.search(r"\d",b[i])
    if d:
        e=re.findall(r".[a-zA-Z]+",b[i])
        if e:
            print("False")
        else:
            print("True")
    else:
        print("False")