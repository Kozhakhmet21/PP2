import re
file=open('text.data','r')
a=file.read()
BINdata=r"\nБИН.*(?P<BIN>\b[0-9]+)"
BINtext=re.search(BINdata,a).group("BIN")
print(BINtext)