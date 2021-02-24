a=3
try:
    print(a)
except NameError:
    print("Variable a isn't defined")
except:
    print("Something else went wrong")