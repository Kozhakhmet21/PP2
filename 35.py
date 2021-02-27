import re
file=open("text.data","r")
text=file.read()
itemPattern=r"\bСтоимость\n(?P<total2>.*)"
itemtext=re.search(itemPattern,text).group("total2")
print(itemtext)