import re
file=open("text.data","r")
text=file.read()
Data=r"Время.*[^\d]*"
x=re.search(Data,text)
b=str(x)
print(b)
i=50
c=[]
for i in range(51,len(b)-24):
    c.append(b[i])
d=''.join(str(x) for x in c)
print(d)