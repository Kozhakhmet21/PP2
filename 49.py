import re
file=open("text.data","r")
text=file.read()
a=r"\nг.*(?P<address>(\b[а-яА-Я]+)-(\b[а-яА-Я]+),(\b[а-яА-Я]+),(.*(\b[а-яА-Я]+).*(\b[а-яА-Я]+)+)-(\b[0-9]+)+)"
item=re.compile(a)
for m in re.finditer(item,text):
    print(m.group("address"))