import re
a="The rain in Spain"
x=re.search("The.*Spain$",a)
print(x)
if x:
    print("Yes")
else:
    print("No")