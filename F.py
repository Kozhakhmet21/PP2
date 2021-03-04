list1=[int(x) for x in input().split()]
a=int(list1[0])
b=int(list1[1])
x=0
while a<=b: # x-bul iteator myndetty turde whiledyn en basty shartynda turum mindetty emes.
    a*=3
    b*=2
    x+=1
print(x)