import numpy as np
import re
from sys import exit


class Wrapper:
    def __init__(self, num):
        self.num = num


mode = ['t20.txt', 'input20.txt']
file = mode[1]
nums  = list(map(int, open(file).read().splitlines()))

numbers = [Wrapper(n) for n in nums]
aux = [w for w in numbers]
for w in numbers:
    print(w.num)
print('')
off = None
for index, w in enumerate(aux):
    if index% 100 == 0:
        print(index, '/', len(numbers))
    if w.num == 0:
        off = w
    # print('Moves: ', w.num)
    pos = numbers.index(w)
    numbers.pop(pos)
    new_pos = (pos + w.num) % len(numbers)
    numbers.insert(new_pos, w)
    
    
    # if w.num >= 0:
    #     for i in range(w.num):
    #         swappos = (pos + i)% len(numbers)
    #         swappos1 = (pos + i+1)% len(numbers)
    #         numbers[swappos], numbers[swappos1] = numbers[swappos1], numbers[swappos]
    # else:
    #     for i in range(-w.num):
    #         swappos = (pos - i)% len(numbers)
    #         swappos1 = (pos - i-1)% len(numbers)
    #         if swappos == 0:
    #             numbers.append(numbers.pop(0))
    #             swappos = -2
    #             pos = numbers.index(w)+i
    #         numbers[swappos], numbers[swappos1] = numbers[swappos1], numbers[swappos]
    # for w in numbers:
    #     print(w.num)
    # print('')
    
imp = [1000, 2000, 3000]


# for w in numbers:
#     print(w.num)
    
offset = numbers.index(off)

x = [numbers[(offset+i)%len(numbers)].num for i in imp]
print(x)
print(sum(x))
        
            
            
    
    
    



    
    
    

            
        
    
    

    


    



 





    


                


       
        


    
    
            
        

        
        
    