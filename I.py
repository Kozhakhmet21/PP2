a=int(input())
b=[int(x) for x in input().split()]
c=int(input())
list1=list()
list2=list()
x=0
if a==len(b):
    for x in range(len(b)):
        if x<c:
            list1.append(b[x])
        else:
            list2.append(b[x])
str1 = ''.join(str(x) for x in list1)
str2 = ''.join(str(y) for y in list2)
print(str1)
print(str2)
print(int(str1)*int(str2))