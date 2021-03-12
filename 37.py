import os
way= '/Users/kozhahmet/PP 2/Week 3'

totalFiles = 0

for files in os.walk(way):
    print(files)