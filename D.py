a=str(input())
list1=[int(x) for x in input().split()]
b=list()
x=y=i=0
for i in range(len(a)):
    b.append(a[i])
l="L"
u="U"
r="R"
d="D"
for i in range(len(b)):
    if b[i]==l:
        x+=-1
    elif b[i]==u:
        y+=1
    elif b[i]==d:
        y+=-1
    elif b[i]==r:
        x+=1
if list1[0]==x and list1==y:
    print("Passed")
else:
    print("Missed")
print(x,y)