import re 
a="The game 1234 over!"
x=re.findall("[^012]",a) #bul ekeuinig aiyrmashylygy y-qana x-ke qaragande tek ' '-probeldy gana joyady.
y=re.findall("[^01 2]",a)
print(x)
print(y)