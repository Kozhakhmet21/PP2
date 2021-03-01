a=int(input())
x=0
b=list()
while x<4:
    c=str(input())
    b.append(c)
    x+=1
for x in range(len(b)):
    if b[x]==["a"-"z"]:
        print(b[x])