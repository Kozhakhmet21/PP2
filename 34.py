import re
file=open("text.data","r")
text=file.read()
itemPattern=r"(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itemtext=re.search(itemPattern,text).group("total1")
print(itemtext)