import os
way= '/Users/kozhahmet/PP 2/Week 5'

totalFiles = 0

for files in os.walk(way):
    for Files in files:
        totalFiles += 1


print('Total number of files',totalFiles)
