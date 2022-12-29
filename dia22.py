import numpy as np
import re
from sys import exit

    

mode = ['t22.txt', 'input22.txt']
file = mode[1]
lines  = open(file).read().splitlines()

space = set()
blocked = set()

path = lines[-1]
lines = lines[:-1]
p = ""
for c in path:
    if c in "RL": p+= f',{c},'
    else: p+= c
p = p.split(',')


for r,line in enumerate(lines):
    for c in range(len(line)):
        if line[c] == '.':
            space.add((r+1, c+1))
        if line[c] == '#':
            blocked.add((r+1, c+1))

def change_dir(d, turn):
    if d == "s":
        if turn == "R":
            return "w"
        return "e"
    if d == "n":
        if turn == "R":
            return "e"
        return "w"
    if d == "w":
        if turn == "R":
            return "n"
        return "s"
    if d == "e":
        if turn == "R":
            return "s"
        return "n"

pos = min(space)
d = "e"



dirs = {"s": (1, 0), "n": (-1, 0),"w": (0, -1),"e": (0, 1)}


for i in range(0, len(p),1):
    turn = steps = None
    if p[i] in "RL":
        turn = p[i]
    else:
        steps = int(p[i])
    if steps:
        for step in range(steps):
            # print("Att", d,"at", pos)
            newpos = (pos[0] + dirs[d][0], pos[1] + dirs[d][1])
            if newpos in space:
                # print("step", d,"at", pos, "to", newpos)
                pos = newpos
            elif newpos in blocked:
                break
            else:
                if d == "s":
                    r,c = newpos
                    same_col = set([p for p in space.union(blocked) if p[1] == c])
                    newpos = min(same_col)
                if d == "n":
                    r,c = newpos
                    same_col = set([p for p in space.union(blocked) if p[1] == c])
                    newpos = max(same_col)
                if d == "w":
                    r,c = newpos
                    same_row = set([p for p in space.union(blocked) if p[0] == r])
                    newpos = max(same_row)
                if d == "e":
                    r,c = newpos
                    same_row = set([p for p in space.union(blocked) if p[0] == r])
                    newpos = min(same_row)
                if newpos in blocked:
                    break
                pos = newpos
                # print("step", d,"at", pos, "to", newpos)
            
    if turn:
        # print("TURN", d, turn)
        d = change_dir(d, turn)
        # print("TO", d)
    

        
# print(pos, d)


dec = {"e": 0,"s": 1,"w": 2,"n": 3}
print(1000*pos[0] + 4*pos[1] + dec[d], d)
    
    



    
    
        
        
            
            
    
    
    



    
    
    

            
        
    
    

    


    



 





    


                


       
        


    
    
            
        

        
        
    