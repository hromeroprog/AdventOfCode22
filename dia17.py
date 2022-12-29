import numpy as np
import re
from sys import exit

mode = ['t17.txt', 'input17.txt']
file = mode[1]
steams  = open(file).read().splitlines()[0]

def getshape(t: int,height):
    if t==0:
        return [(i,height) for i in range(2, 6)]
    elif t == 1:
        return [(3,height),(3,height+1),(3,height+2),(2,height+1),(4,height+1)]
    elif t == 2:
        shape = [(i,height) for i in range(2, 5)] + [(4,height+1),(4,height+2)]
        return shape
    elif t == 3:
        return [(2, i) for i in range(height, height+4)]
    elif t == 4:
        return [(2,height), (3,height), (2, height+1), (3, height+1)]

    
shapes = 0
curr_h = 0
blocked_points = set([(i,0) for i in range(7)])
cont = 0
while shapes < 2022:
    t = shapes %5
    shape = getshape(t, curr_h+4)
    shapes += 1
    #moveshape
    # print('New shape', shape)
    
    while True:
        #steam
        s = steams[cont%len(steams)]
        cont+=1
        if s =='<': 
            new_shape = [(i-1,j) for i,j in shape]
            if min([i for i,j in new_shape]) >= 0 and not any((i,j) in blocked_points for i,j in new_shape):
                shape = new_shape
                # print('move left', shape)
        if s =='>':
            new_shape = [(i+1,j) for i,j in shape]
            if max([i for i,j in new_shape]) <= 6 and not any((i,j) in blocked_points for i,j in new_shape):
                shape = new_shape
                # print('move right', shape)
        if any((i,j-1) in blocked_points for i,j in shape):
            # print('blocked')
            for p in shape:
                blocked_points.add(p)
            curr_h = max([j for i,j in blocked_points])
            break
        shape = [(i, j-1) for i,j in shape]
        # print('move down')

print(curr_h)        
            
height = max([j for i,j in blocked_points])

result = ""
# for j in range(height,0,-1):
#     for i in range(7):
#         result += "#" if (i,j) in blocked_points else "."
#     result += "\n"

# print(result)
    
    
    

            
        
    
    

    


    



 





    


                


       
        


    
    
            
        

        
        
    