import re
a="The 34 56 6 rain9 in Spain"
x=re.findall("[0-5][0-9]",a) # 00-59 osy aralyqtagy sandardy shygardy
print(x)