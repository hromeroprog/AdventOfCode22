import numpy as np
import re
from sys import exit

mode = ['t18.txt', 'input18.txt']
file = mode[1]
lines  = open(file).read().splitlines()


    
class Cube:
    def __init__(self, pos):
        self.points = set()
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    self.points.add((pos[0]+x, pos[1]+y, pos[2]+z))
        
cubes = [Cube(tuple(map(int, re.findall(r"-*\d+", line)))) for line in lines]

exposed = 6*len(cubes)
for i in range(len(cubes)-1):
    for j in range(i+1, len(cubes)) :
        collide = cubes[i].points & cubes[j].points
        if len(collide) ==4:
            # print("\n\n", collide, "\n\t",cubes[i].points,"\n\t" ,cubes[j].points)
            exposed -= 2
print(exposed)
            
        
    
    

    


    



 





    


                


       
        


    
    
            
        

        
        
    