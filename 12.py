def func(a):
    i=1
    c=0
    b=[]
    while i<a:
        if a%i==0:
            b.append(i)
        i+=1
    for i in range(0,len(b)):
        c+=b[i]
    if c==a:
        print("Yes, the number is perfect.")
    else:
        print("No, the number is not perfect.")

a=int(input())
func(a)