import itertools   
      
# using repeat() to repeatedly print number   
print ("Printing the numbers repeatedly : ")   
print (list(itertools.repeat(25, 8*100))) 




''' import itertools  
    
count = 0
    
# for in loop  
for i in itertools.cycle('AB'):  
    if count > 7:  
        break
    else:  
        print(i, end = " ")  
        count += 1
'''
