a=int(input())
b=set(map(str,input().split())) #differce fun. tek set() ushin gana arnalgan.
c=int(input())
d=set(map(str,input().split())) #Eger biz **list2 dep []-syz jazsaq onda ol arasyna ashyp stroka elementyn,yagny aripty bolek jazazdt
x=0
diff1=b.difference(d)
list1=list(diff1)
diff2=d.difference(b)
list2=list(diff2)
for x in range(len(list1)):
    print("Missed students:")
    print("-",list1[x])
for x in range(len(list2)):
    print("Not in the group:")
    print("-",list2[x])