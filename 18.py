import os
import fnmatch
a="/Users/kozhahmet/PP 2/Week 5"
with os.scandir(a) as b:
    for items in b:
        if items.is_file():
            print(items.name)