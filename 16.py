def func(a):
    b=set()
    c=a.lower()
    for i in range(len(c)):
        if c[i]!=' ':
            b.add(c[i])
    if len(b)==26:
        print("Yes, string is a pangram")
    else:
        print("No, string is not a pangram")
a=str(input())
func(a)