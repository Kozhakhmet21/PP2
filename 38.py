import re
import csv

file=open("text.data","r")
text=file.read()
BINPattern=r"\nБИН.*(?P<BIN>\b[0-9]+)"
NDSPattern=r"\nНДС.*(?P<NDS>\b[0-9]+)"
BINtext=re.search(BINPattern,text).group("BIN")
NDStext=re.search(NDSPattern,text).group("NDS")
itemPatterntext=r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itemPattern=re.compile(itemPatterntext)
items=[["БИН","НДС","Наименование товара","Кол-во","Цена за единиц"]]
for m in re.finditer(itemPattern,text):
    items.append([BINtext,NDStext,m.group("name"),m.group("count"),m.group("price")])
with open("file.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerows(items)
file.close()