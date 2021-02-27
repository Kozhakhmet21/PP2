import re
file=open("text.data","r")
text=file.read()
Comp=r"\nФилиал.*(?P<NCompany>\b[a-zA-Z]+)"
Comptext=re.compile(Comp)
for m in re.finditer(Comptext,text):
    print(m.group("NCompany"))