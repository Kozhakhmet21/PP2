def func(a):
    cnt1=0
    cnt2=0
    for i in range(len(a)):
        if a[i]>='A' and a[i]<='Z':
            cnt1+=1
        elif a[i]>='a' and a[i]<='z':
            cnt2+=1
    return cnt1,cnt2
a=str(input())
b=func(a)
print("Upper case characters:", b[0])
print("Lower case Characters:",b[1])