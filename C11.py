min=4
for i in range(0,4):
    if (i % 2!=0) and (i % 3 ==0)and (i % 5 ==0)and (i % 7 ==0)and (i % 9 ==0)and (i <min):
        min=i
print(min)