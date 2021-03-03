import os

def walk(a):
    for x in os.walk(a):
        for x in os.walk(a):
            print(x)
folders=walk('/Users/kozhahmet/PP 2/Week 6')
print(folders)

#Osylai biz bukil folders, files, barlyq elementerdy shygardyq.