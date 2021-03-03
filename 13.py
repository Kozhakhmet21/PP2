import os
def read():
    currentPath=os.getcwd()
    with open(os.path.join(currentPath,'experiment/sum.txt'),'r') as b:
        print(b)
        line=b.readline()
        nums=line.split(' ')
        return nums
a=read()
print(a)