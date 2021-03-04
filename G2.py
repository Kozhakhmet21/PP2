import re
a=[str(x) for x in input().split()]
c=str(input())
e=str(input())
g=str(input())
f=[]
j=0
for i in range(len(a)):
    x=re.search(c,a[i])
    if x:
        d=a[i].replace(c,e)
        f.append(d)
    else:
        f.append(a[i])
for i in range(len(f)):
    y=re.search(g,f[i])
    if y:
        print(f[i])
        j+=1
print(j)

#Osylai meily kerek element .,?! tagy basqa elemebt bolsyn.
#Jalpy g degen soz bolsa artyq symboldarmen bolsyn, ol osy argyly sanai beredy.