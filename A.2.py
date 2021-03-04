import re
a=str(input())
b=r"\b[A-Z]"
x=re.search(b,a)
if x:
    print("Found a match!")
else:
    print("Not matched!")
print(b)