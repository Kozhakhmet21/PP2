import os
def read():
    currentPath=os.getcwd()
    with open(os.path.join(currentPath,'experiment/sum.txt'),'r') as b:
        print(b)
        line=b.readline()
        nums=line.split(' ')
        Sum=0
        for x in nums:
            c=int(x)
            Sum+=c
        return Sum
a=read()
print(a)