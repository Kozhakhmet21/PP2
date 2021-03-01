import re
file=open("text.data","r")
text=file.read()
a=r"Время.*(.*(\b[0-9]+).(\b[0-9]+).(\b[0-9]+).(\b[0-9]+).*(\b[0-9]+):(\b[0-9]+)+)"
x=re.search(a,text)
print(x)
print(x.groups())