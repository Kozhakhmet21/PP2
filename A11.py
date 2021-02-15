a=input()
b=input()
x=1
while x<=a:
    if a%x==0:
        c=x
    elif b%x==0:
        d=x
    if c==d:
        print(x)       
    x+=1