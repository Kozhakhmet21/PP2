import re
import csv

file=open("text.data","r")
text=file.read()
Comp=r"\nФилиал.*(?P<NCompany>\b[a-zA-Z]+)"
BINPattern=r"\nБИН.*(?P<BIN>\b[0-9]+)"
NDSPattern=r"\nНДС.*(?P<NDS>\b[0-9]+)"
TimePattern=r"Время.*(?P<time>.*(\b[0-9]+).(\b[0-9]+).(\b[0-9]+).(\b[0-9]+).*(\b[0-9]+):(\b[0-9]+)+)"
AddressPattern=r"\nг.*(?P<address>(\b[а-яА-Я]+)-(\b[а-яА-Я]+),(\b[а-яА-Я]+),(.*(\b[а-яА-Я]+).*(\b[а-яА-Я]+)+)-(\b[0-9]+)+)"
Comptext=re.search(Comp,text).group("NCompany")
BINtext=re.search(BINPattern,text).group("BIN")
NDStext=re.search(NDSPattern,text).group("NDS")
Timetext=re.search(TimePattern,text).group("time")
Addresstext=re.search(AddressPattern,text).group("address")
itemPatterntext=r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itemPattern=re.compile(itemPatterntext)
items=[["Филиал ТОО","БИН","НДС","Наименование товара","Кол-во","Цена за единиц","Время","Адрес"]]
for m in re.finditer(itemPattern,text):
    items.append([Comptext,BINtext,NDStext,m.group("name").strip(),m.group("count").strip(),m.group("price").strip(),Timetext,Addresstext])
with open("file.csv5","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerows(items)
file.close()