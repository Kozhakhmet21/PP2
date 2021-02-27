import re
file=open("text.data","r")
text=file.read()
itemPatterntext=r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}"
itemPattern=re.compile(itemPatterntext)
for m in re.finditer(itemPattern,text):
    print(m.group("name")+" "+m.group("count")+m.group("price"))
file.close()