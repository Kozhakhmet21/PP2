import re
a=str(input())
b="qwrtpsdfghjklzxcvbnm"
c="aeiou"
match=re.findall(r'(?<=['+b+'])(['+c+']{2,})(?=['+b+'])',a,flags=re.I)
if match:
    for i in match:
        print(i)
else:
    print(-1)