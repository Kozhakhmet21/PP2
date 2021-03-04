import re
a=str(input())
b="_"
x=re.findall(b,a)
if x:
    print("Found a match!")
else:
    print("Not matched!")