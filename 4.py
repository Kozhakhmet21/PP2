import re
a=str(input())
x=re.findall(r"\w+",a)
b=re.findall(r"(?P<vowels>.*aieou)",x)