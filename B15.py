with open('BB15') as datfile:
    text = datfile.read()
print(sum(map(int, text.split(None, 2)[:2])))
