import re
a="The rain in Spain"
x=re.findall("[a-h]",a)
if x:
    print("Yes")
else:
    print("No")
print(x)