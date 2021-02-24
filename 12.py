import re 
a="The rain in Spain 1234"
x=re.search(r"(?P<a1>.+)(?P<a2>\b[0-9]+)",a) # <-- Baganan bery qate boldy sebeby bul jerde aty qoyatyn kezde group a1 jane group a2 dep at qoiuga bolmaidy.
print(x.group("a1"))
print(x.group("a2"))