import os
def read():
    currentPath=os.getcwd()
    with open(os.path.join(currentPath,'/Users/kozhahmet/PP 2/Week 6/experiment/sum.txt')) as b:
        line=b.readline()
        print(line)
        nums=line.split(' ')
        Sum=0
        for x in nums:
            c=int(x)
            Sum+=c
        return Sum
a=read()
print(a)