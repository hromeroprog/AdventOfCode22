import numpy as np
import re
from sys import exit
import time

mode = ['t17.txt', 'input17.txt']
file = mode[1]
steams  = open(file).read().splitlines()[0]
steams = [-1 if c == '<' else +1 for c in steams]

def getshape(t: int,height):
    if t==0:
        return [(i,height) for i in range(2, 6)],(-2,1)
    elif t == 1:
        return [(3,height),(3,height+1),(3,height+2),(2,height+1),(4,height+1)],(-2,2)
    elif t == 2:
        shape = [(i,height) for i in range(2, 5)] + [(4,height+1),(4,height+2)],(-2,2)
        return shape
    elif t == 3:
        return [(2, i) for i in range(height, height+4)],(-2,4)
    elif t == 4:
        return [(2,height), (3,height), (2, height+1), (3, height+1)],(-2,3)

    
shapes = 0
curr_h = 0

cont = 0
tot1  = 1000_000_000_000
tot = 20_000
# tot1 = tot
# tot1 = 5268
start = time.time()

i = 0
# 
blocked_points = set([(i,0) for i in range(7)])

while shapes < 1757:
    if shapes%1000 == 0:
        print(shapes)
    t = shapes %5
    shape,boundaries = getshape(t, curr_h+4)
    shapes += 1
    #moveshape
    # print('New shape', shape)
    # first_down = 3
    # steamres = sum(steams[cont:cont+3])
    # steamres = max(boundaries[0], steamres)
    # steamres = min(boundaries[1], steamres)
    # # print(steamres)
    # shape = [(i+steamres,j-3) for i,j in shape]
    # cont = (cont + 3) % len(steams)
    while True:
        #steam
        s = steams[cont]
        cont = (cont +1) % len(steams)
        
        if s ==-1: 
            new_shape = [(i-1,j) for i,j in shape]
            if min([i for i,j in new_shape]) >= 0 and not any((i,j) in blocked_points for i,j in new_shape):
                shape = new_shape
                # print('move left', shape)
        if s ==1:
            new_shape = [(i+1,j) for i,j in shape]
            if max([i for i,j in new_shape]) <= 6 and not any((i,j) in blocked_points for i,j in new_shape):
                shape = new_shape
                # print('move right', shape)
        if any((i,j-1) in blocked_points for i,j in shape):
            # print('blocked')
            if cont == 33:
                print('Bucle de steams: t = ', t, cont, 'fig', shapes)
                if max([j for i,j in shape]) > curr_h:
                    print('Bucle y nuevo maximo', max([j for i,j in shape]))
                    print()
                
                    # print('Primer punto con steam', shapes, shape ,cont)
                    if shapes != 6 and t == 0:
                        print('Patron encontrado')
                        exit(0)
            
            for p in shape:
                blocked_points.add(p)
                
            for j in set([j for _,j in shape]):
                if all((i,j) in blocked_points for i in range(7)):
                    for elem in list(blocked_points):
                        if elem[1] < j:
                            blocked_points.discard(elem)
            curr_h = max(curr_h,max([j for i,j in shape]))
            break
        shape = [(i, j-1) for i,j in shape]
        # print('move down')

print(curr_h, max((j for _,j in blocked_points)))
print(shapes, 'shape')

print('DESPLAZAR')


for i in range(tot1, 0, -1):
    if i%1755 == 2:
        shapes = i
        print('Shape', shapes)
        curr_h = 2738 + 2768*((i-2)//1755 - 1)
        break

# shapes -= 1755
cont = 33
diff = curr_h - max((j for _,j in blocked_points))

new_blocked_points = set()
for p in blocked_points:
    new_blocked_points.add((p[0], p[1] + diff))

blocked_points = new_blocked_points

print(curr_h, max((j for _,j in blocked_points)))

print('Final simulation', shapes)
while shapes < tot1:
    if shapes%1000 == 0:
        print(shapes)
    t = shapes %5
    shape,boundaries = getshape(t, curr_h+4)
    shapes += 1
    #moveshape
    # print('New shape', shape)
    # first_down = 3
    # steamres = sum(steams[cont:cont+3])
    # steamres = max(boundaries[0], steamres)
    # steamres = min(boundaries[1], steamres)
    # # print(steamres)
    # shape = [(i+steamres,j-3) for i,j in shape]
    # cont = (cont + 3) % len(steams)
    while True:
        #steam
        s = steams[cont]
        cont = (cont +1) % len(steams)
        
        if s ==-1: 
            new_shape = [(i-1,j) for i,j in shape]
            if min([i for i,j in new_shape]) >= 0 and not any((i,j) in blocked_points for i,j in new_shape):
                shape = new_shape
                # print('move left', shape)
        if s ==1:
            new_shape = [(i+1,j) for i,j in shape]
            if max([i for i,j in new_shape]) <= 6 and not any((i,j) in blocked_points for i,j in new_shape):
                shape = new_shape
                # print('move right', shape)
        if any((i,j-1) in blocked_points for i,j in shape):
            # print('blocked')
            if cont == 33:
                print('Bucle de steams: t = ', t, cont, 'fig', shapes)
                if max([j for i,j in shape]) > curr_h:
                    print('Bucle y nuevo maximo', max([j for i,j in shape]))
                    print()
                
                    # print('Primer punto con steam', shapes, shape ,cont)
                    if shapes != 6 and t == 0:
                        print('Patron encontrado')
                        exit(0)
            
            for p in shape:
                blocked_points.add(p)
                
            for j in set([j for _,j in shape]):
                if all((i,j) in blocked_points for i in range(7)):
                    for elem in list(blocked_points):
                        if elem[1] < j:
                            blocked_points.discard(elem)
            curr_h = max(curr_h,max([j for i,j in shape]))
            break
        shape = [(i, j-1) for i,j in shape]
        # print('move down')

print(curr_h)        
            
height = max([j for i,j in blocked_points])
min_height = min([j for i,j in blocked_points])

result = ""
# for j in range(height,min_height,-1):
#     for i in range(7):
#         result += "#" if (i,j) in blocked_points else "."
#     result += "\n"

# print(result)
    
end = time.time()

print('Took' ,end- start,"seg", height)




    

            
        
    
    

    


    



 





    


                


       
        


    
    
            
        

        
        
    