import re
file=open('text.data','r')
a=file.read()
x=re.search(r"\nБИН.*",a)
print(x)