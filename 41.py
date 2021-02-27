import re
file=open("text.data","r")
text=file.read()
Comp=r"\nФилиал ТОО.*(?P<NCompany>\b[a-zA-Z]+)"
Comptext=re.search(Comp,text)
print(Comptext)