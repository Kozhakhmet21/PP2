import re
file=open("text.data","r")
text=file.read()
Time=r"\nг.*(?P<data>\w)+"
timetext=re.compile(Time)
for m in re.finditer(timetext,text):
    print(m.group("data"))