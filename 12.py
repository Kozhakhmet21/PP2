import re
file=open("text.data","r")
text=file.read()
x=re.search(r"(?P<text>(.*\n{1})+)+",text)
print(x.group("text"))q