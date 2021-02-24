import re
a="The Spain"
x=re.split("\s",a)
if x:
    print("yes")
else:
    print("no")
print(x)