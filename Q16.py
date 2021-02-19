def fun(**kw):
    key=input()
    c=str(key)
    for c in kw:
        print(key)

a={
    "Russia":"Moscow",
    "Ukraine":"Kiev"
}
fun(**a)