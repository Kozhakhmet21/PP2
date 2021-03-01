import re
file=open("text.data","r")
text=file.read()
a=r"\nг.*((\b[а-яА-Я]+)-(\b[а-яА-Я]+),(\b[а-яА-Я]+),(\b[а-яА-Я]+).*(\b[а-яА-Я]+),(\b[0-9]+),(\b[а-яА-Я]+)-(\b[0-9]+)+)"
x=re.search(a,text)
print(x)
print(x.group()