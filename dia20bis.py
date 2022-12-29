import numpy as np
import re
from sys import exit


class Wrapper:
    def __init__(self, num):
        self.num = num


mode = ['t20.txt', 'input20.txt']
file = mode[1]
nums  = list(map(int, open(file).read().splitlines()))

key = 811589153
numbers = [Wrapper(n*key) for n in nums]
aux = [w for w in numbers]
for w in numbers:
    print(w.num)
    
print('')
for _ in range(10):
    off = None
    for index, w in enumerate(aux):
        if index% 1000 == 0:
            print(index, '/', len(numbers))
        
        # print('Moves: ', w.num)
        pos = numbers.index(w)
        numbers.pop(pos)
        new_pos = (pos + w.num) % len(numbers)
        numbers.insert(new_pos, w)

for index, w in enumerate(numbers):
    if w.num == 0:
        print('0 at ', index)
        off = w
    
    
imp = [1000, 2000, 3000]


for w in numbers:
    print(w.num)
    
offset = numbers.index(off)

x = [numbers[(offset+i)%len(numbers)].num for i in imp]
print(x)
print(sum(x))
        
            
            
    
    
    



    
    
    

            
        
    
    

    


    



 





    


                


       
        


    
    
            
        

        
        
    