import re
file=open("text.data","r")
text=file.read()
itemPatterntext=r"(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)" #Myna jerde total1 men total2 ulken ayrmarshylygy jok.
itemPattern=re.compile(itemPatterntext)
for m in re.finditer(itemPattern,text):
    print(m.group("total2"))