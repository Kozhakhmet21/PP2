a=[7,5,9,8,53,45,34,32,56]
b=list(filter(lambda x:x%2!=0,a))
print(b)
c=tuple(filter(lambda y:y%2==0,a))
print(c)