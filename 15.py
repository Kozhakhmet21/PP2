import re
a="The rain all the world in Spain go as fall in sky"
x=re.findall("al{2}",a)
y=re.findall("all{5}",a) #all degen 5-ret qaitalanyp turgan jok.
print(x)
print(y)