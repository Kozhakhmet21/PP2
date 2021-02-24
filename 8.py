import re
a="The 345 rain45 in Spain" # \d osygan qarama-qarsy eger qatarda san bolsa ony almai tek san emesterdy barin alady.
x=re.findall("\D",a)
print(x)