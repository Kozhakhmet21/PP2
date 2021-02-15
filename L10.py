a=[int(i) for i in input().split()]
for x in range(1,len(a),2):
    a[x-1],a[x]=a[x],a[x-1]
print(" ".join([str(i) for i in a]))