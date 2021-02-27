import re
file=open("text.data","r")
text=file.read()
BINPattern=r"\nБИН.*(?P<BIN>\b[0-9]+)"
NDSPattern=r"\nНДС.*(?P<NDS>\b[0-9]+)"
BINtext=re.search(BINPattern,text).group("BIN")
NDStext=re.search(NDSPattern,text).group("NDS")
print(BINtext)
print(NDStext)