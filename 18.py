import re
a="Ain The main rain in Spain"
x=re.findall(r"\bAin",a)
y=re.findall(r"\bSpain",a)
z=re.findall(r"\bain",a) # \b bul tek eger sonyn qasynda qosylyp jazylgan bolik strokadagy sozderde izdeidy.
print(x) # Eger osy basy bolyp bastalnyp tur ma, sony izdeidy basy solai bastalsa true qaitarady.
print(y)
print(z)