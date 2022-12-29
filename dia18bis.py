import numpy as np
import re
from sys import exit

mode = ['t18.txt', 'input18.txt']
file = mode[1]
lines  = open(file).read().splitlines()

class Cube:
    def __init__(self, pos):
        self.pos = pos
        self.points = set()
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    self.points.add((pos[0]+x, pos[1]+y, pos[2]+z))
     
    
    def getcaras(self):
        caras = []
        for x in range(2):
            caras.append(sorted([point for point in self.points if point[0] == x+self.pos[0]]))
        for y in range(2):
            caras.append(sorted([point for point in self.points if point[1] == y+self.pos[1]]))
        for z in range(2):
            caras.append(sorted([point for point in self.points if point[2] == z+self.pos[2]]))
        self.caras = sorted(caras)
        return sorted(caras)
    
    def hasarista(self):
        pass
        

# class Sup:
#     def __init__(self):
        
def distancia(cara, cara1):
    # print("Calculando distancia", cara, "a", cara1)
    meancara = np.array(cara).mean(axis = 0)
    meancara1 = np.array(cara1).mean(axis = 0)
    d = np.linalg.norm(meancara-meancara1)
    # print("d=", d)
    return d
    
def same_cube(cara,cara1,cubes):
    for cube in cubes:
        if cara in cube.caras and cara1 in cube.caras:
            return True
    # print("Differente cube")
    return False
        
cubes = [Cube(tuple(map(int, re.findall(r"-*\d+", line)))) for line in lines]
caras = []

for cube in cubes:
    caras += cube.getcaras()
    
free_caras = [cara for cara in caras if caras.count(cara) == 1]

start = min(free_caras)
queue = [start]
finished = []
caras = [cara for cara in free_caras]
total = 0
print("Start", start)
while queue:
    n = queue.pop(0)
    total += 1
    finished.append(n)
    #Generar movimientos de hormiga
    for i in range(len(n)-1):
        for j in range(i+1, len(n)):
            arista = n[i], n[j]
            caras_compartidas = []
            for cara in caras:
                if cara != n and arista[0] in cara and arista[1] in cara:
                    caras_compartidas.append(cara)
            if len(caras_compartidas) == 1:
                cand = caras_compartidas[0]
                if cand not in queue and cand not in finished:
                    queue.append(cand)
            elif caras_compartidas:
                cand = sorted(caras_compartidas, key = lambda x: (1-same_cube(n, x, cubes))/distancia(n,x), reverse = True)[0]
                if cand not in queue and cand not in finished:
                    queue.append(cand)
            
                    
        
    
        
            
            
    
print(total)        
        
    
    

    


    



 





    


                


       
        


    
    
            
        

        
        
    