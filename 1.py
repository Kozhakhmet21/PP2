import re
a="The rain in Span"
x = re.search('^The.*Span$',a) #$-stroka osy elementten aqtalsa.
if x:
    print("Yes, it is exist")
else:
    print("No, it doesn't exist")
print(x)