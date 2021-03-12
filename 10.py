def func(a):
    cnt=0
    i=1
    while i<=a:
        if a%i==0:
            cnt+=1
        i+=1
    if cnt==2:
        print("YES")
    else:
        print("NO")

a=int(input())
func(a)