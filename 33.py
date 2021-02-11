def f(**kwargs):
    for a in kwargs:
        print(a)
a={
    "1":2,
    "3":4,
    "8":9
}
f(**a)