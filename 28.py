import re
file=open('text.data','r')
a=file.read()
BIN=r'\nБИН.*(\b[0-9]+)'
x=re.search(BIN,a)
print(x.group(1))