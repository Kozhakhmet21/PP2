def func(a):
    cnt=0
    for i in range(0,len(a)):
        if a[i]==a[len(a)-1-i]:
            cnt+=1
    if cnt==len(a):
        print("YES")
    else:
        print("NO")
a=str(input())
func(a)