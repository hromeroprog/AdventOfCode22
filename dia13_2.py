import numpy as np
import ast

mode = ['t.txt', 'input.txt']
file = mode[0]
lines  = open(file).read().splitlines()
lines = [[lines[i],lines[i+1]] for i in range(0, len(lines), 3)]

                     
total = 0
for i,case in enumerate(lines):
    st1 = case[0].replace('[','').replace(' ', '').replace(']', '').replace(',', '')
    st2 = case[1].replace('[','').replace(' ', '').replace(']', '').replace(',', '')
    if st1<=st2:
        print('True CASE #', i+1)
        total += i+1
        print(st1, st2)
        print(case[0], case[1])

print(total)



    


                


       
        


    
    
            
        

        
        
    