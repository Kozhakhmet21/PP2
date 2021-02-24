import re
a="The main of my lis is be carefull and sea to future very well and don't worry"
x=re.findall("stay|well",a)
y=re.findall("stay|ll",a)
print(x)
print(y)