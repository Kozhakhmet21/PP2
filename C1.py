a=int(input())
b=[int(x) for x in input().split()]
c=set()
for x in range(len(b)):
    c.add(b[x])
if len(c)==a:
    print("YES")
else:
    print("NO")
# Mindetty turde C++ sekildy massivetyg razmerymen gane element engyzudyn qazhety zhoq, ondai python ushin tiymsyz.