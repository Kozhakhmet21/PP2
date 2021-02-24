import re
file=open('text.data','r')
a=file.read()
BIN=r"\nБИН(.*)"
x=re.search(BIN,a)
print(x.group(1))
file.close()