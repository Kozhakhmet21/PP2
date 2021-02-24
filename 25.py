import re
a="The rain in Spain 1234"
x=re.search(r"(.+)([0-9]+)",a)
print(x.group())
print(x.groups()) #grou.p() pen groups() ekeuinde de ulken ayrmashylyq bar.