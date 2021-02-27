import re
file=open("text.data","r")
text=file.read()
BIN=r"\nБИН.*(\b[0-9]+)"
x=re.search(BIN,text)
print(x.group(1))