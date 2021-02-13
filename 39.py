def f(a):
    print(a[0])
    for x in range(len(a)):
      if x==len(a)-1:
          print(a[x])

f([2,4,6,8])