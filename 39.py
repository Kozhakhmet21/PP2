import re
import csv

file=open("text.data","r")
text=file.read()
Comp=r"\nФилиал.*(?P<NCompany>\b[a-zA-Z]+)"
BINPattern=r"\nБИН.*(?P<BIN>\b[0-9]+)"
NDSPattern=r"\nНДС.*(?P<NDS>\b[0-9]+)"
Comptext=re.search(Comp,text).group("NCompany")
BINtext=re.search(BINPattern,text).group("BIN")
NDStext=re.search(NDSPattern,text).group("NDS")
itemPatterntext=r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itemPattern=re.compile(itemPatterntext)
items=[["Филиал ТОО","БИН","НДС","Наименование товара","Кол-во","Цена за единиц"]]
for m in re.finditer(itemPattern,text):
    items.append([Comptext,BINtext,NDStext,m.group("name").strip(),m.group("count").strip(),m.group("price").strip()])
with open("file.csv2","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerows(items)
file.close()