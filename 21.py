def pr(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

a=[1,2,6,7,34,23,21,11,9,898,98,1,1001,101,67]
b=tuple(filter(pr,a))
print(b)
c=list(filter(lambda x:pr(x),a))
print(c)