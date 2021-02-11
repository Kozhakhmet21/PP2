a=[1,2,3,4,4,4,5,5,5,6,6,77,7,7,7,7,8,9,9,10]
b=dict()
for i in a:
    if i not in b:
        b[i]=0
    b[i]+=1
print(b)