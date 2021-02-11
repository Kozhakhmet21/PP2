a=input()
b=input()
c=input()
d=a**2+b**2
if c**2==d :
    print("rectangular")
elif a==b==c:
    print("acute")
elif c!=a+b:
    print("obtuse")
else:
    print("impossibl")