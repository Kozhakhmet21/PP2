a=int(input())
b=[str(x) for x in input().split()] #Bulai list engizip differncepen jumys jasauga bolmaidy. Ony mappen jasu kerek.
c=int(input())
d=[str(x) for x in input().split()]
diff1=b.difference(d)
list1=list(diff1)
for i in range(len(list1)):
    print("-",list1[i])