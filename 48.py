import re
file=open("text.data","r")
text=file.read()
a=r"Время.*(?P<time>.*(\b[0-9]+).(\b[0-9]+).(\b[0-9]+).(\b[0-9]+).*(\b[0-9]+):(\b[0-9]+)+)"
item=re.compile(a)
for m in re.finditer(item,text):
    print(m.group("time"))