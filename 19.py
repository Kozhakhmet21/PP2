import os
import fnmatch
a="/Users/kozhahmet/PP 2/Week 6"
with os.scandir(a) as b:
    for item in b:
        if item.is_file():
            if fnmatch.fnmatch(item.name,"*.py"):
                print(f"____{item.name}")
                file=open(item.name)
                c=file.read()
                print(c)