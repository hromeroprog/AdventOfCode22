import numpy as np
import re
from sys import exit

    

mode = ['t23.txt', 'input23.txt']
file = mode[1]
lines  = open(file).read().splitlines()

class Elf:
    def __init__(self, pos):
        self.pos = pos
        # self.order = ["n", "s", "w", "e"]
    
    def proposition(self, elves, proposes, order):
        self.propose = None
        if not any([(self.pos[0] + i,self.pos[1]+j)in elves for i in range(-1, 2) for j in range(-1, 2) if not (i == j == 0)]):
            return
        for o in order:
            if o == "n":
                if not any([(self.pos[0] -1,self.pos[1]+j)in elves for j in range(-1, 2)]):
                    self.propose = (self.pos[0]-1, self.pos[1])
                    break
            elif o == "s":
                if not any([(self.pos[0] +1,self.pos[1]+j)in elves for j in range(-1, 2)]):
                    self.propose =(self.pos[0]+1, self.pos[1])
                    break
            elif o == "w":
                if not any([(self.pos[0] + j,self.pos[1]-1)in elves for j in range(-1, 2)]):
                    self.propose =(self.pos[0], self.pos[1]-1)
                    break
            elif o == "e":
                if not any([(self.pos[0] + j,self.pos[1]+1)in elves for j in range(-1, 2)]):
                    self.propose= (self.pos[0], self.pos[1]+1)
                    break
        if self.propose:
            if self.propose not in proposes:
                proposes[self.propose] = 0
            proposes[self.propose] += 1
             
        

positions = set()

elves = []
order = ["n", "s", "w", "e"]
rounds = 0

for r,line in enumerate(lines):
    for c,char in enumerate(line):
        if char == "#":
            positions.add((r, c))
            elves.append(Elf((r, c)))

while True:
    rounds += 1
    proposes = {}
    for elf in elves:
        elf.proposition(positions, proposes, order)
    
    change = False
    
    for elf in elves:
        if elf.propose and elf.propose in proposes and proposes[elf.propose] == 1:
            positions.remove(elf.pos)
            positions.add(elf.propose)
            elf.pos = elf.propose
            change = True
    if not change:
        print(rounds)
        break
    order.append(order.pop(0))


    


    
    
        
        
            
            
    
    
    



    
    
    

            
        
    
    

    


    



 





    


                


       
        


    
    
            
        

        
        
    