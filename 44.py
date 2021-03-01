import re
file=open("text.data","r")
text=file.read()
address=re.search(r"г. Нур.*(\w+)",text)
e=str(address)
i=0
f=[]
for i in range(44,len(e)-2):
    f.append(e[i])
g=''.join(str(x) for x in f)
print(g)