import re
a="The reain in Spain"
x=re.sub("\s","-",a)
if x:
    print("yes")
else:
    print("no")
print(x)