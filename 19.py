import re
x="The rain in Spain"
a=re.search(r"\bS\w+",x) #osylai tapqan elementy birden grupalauga bolady.
print(a.group())