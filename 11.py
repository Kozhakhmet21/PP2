import re
a="The rain 34 in Spain 123"
x=re.search(r"(.+)([0-9]+)",a)
print(x)
print(x.group(1))
print(x.group(2))