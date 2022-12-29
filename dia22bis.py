import numpy as np
import re
from sys import exit

mode = ['t22.txt', 'input22.txt']
m = 1
file = mode[m]
lines  = open(file).read().splitlines()

l = 50



space = set()
blocked = set()

path = lines[-1]
lines = lines[:-1]
p = ""
for c in path:
    if c in "RL": p+= f',{c},'
    else: p+= c
p = p.split(',')


faces = {}
for r,line in enumerate(lines):
    for c in range(len(line)):
        if line[c] == '.':
            space.add((r+1, c+1))
            key = 3*int(r/l) + int(c/l)
            if key not in faces:
                faces[key] = set()
            faces[key].add((r+1, c+1))
        if line[c] == '#':
            blocked.add((r+1, c+1))
            key = 3*int(r/l) + int(c/l)
            if key not in faces:
                faces[key] = set()
            faces[key].add((r+1, c+1))

faces = {i+1:faces[f] for i,f in enumerate(faces.keys())}
        
        

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

swaps = {(1,"e"):(2,"e"),(1,"s"):(3,"s"),(1,"w"):(4,"e", "rtoc"),(1,"e"):(2,"e"),}


for i in range(0, len(p),1):
    turn = steps = None
    if p[i] in "RL":
        turn = p[i]
    else:
        steps = int(p[i])
    if steps:
        for step in range(steps):
            # print("Att", d,"at", pos)
            print(pos)
            newpos = (pos[0] + dirs[d][0], pos[1] + dirs[d][1])
            if newpos in space:
                # print("step", d,"at", pos, "to", newpos)
                pos = newpos
            elif newpos in blocked:
                break
            else:
                if pos in faces[1]:
                    print(1)
                    if d == "w":
                        r, c = pos
                        newc = min(faces[4])[1]
                        newr = max(faces[4])[0] - (r - min(faces[1])[0])
                        newpos = (newr, newc)
                        if newpos in blocked:
                            break
                        pos = newpos
                        d = "e"
                    elif d == "n":
                        r, c = pos
                        newc = min(faces[6])[1]
                        newr = min(faces[6])[0] + (c - min(faces[1])[1])
                        newpos = (newr, newc)
                        if newpos in blocked:
                            break
                        pos = newpos
                        d = "e"
                    if newpos[0] * newpos[1] < 0: exit(0)
                elif pos in faces[2]:
                    print(2)
                    if d == "n":
                        r, c = pos
                        newc = min(faces[6])[1] + (c - min(faces[2])[1])
                        newr = max(faces[6])[0]
                        newpos = (newr, newc)
                        print(pos, newpos, "n")
                        if newpos in blocked:
                            break
                        pos = newpos
                        d = "n"
                        pos = newpos
                    elif d == "s":
                        r, c = pos
                        newc = max(faces[3])[1]
                        newr = min(faces[3])[0] + c - min(faces[2])[1]
                        newpos = (newr, newc)
                        print(pos, newpos, "s")
                        if newpos in blocked:
                            break
                        pos = newpos
                        d = "w"
                    elif d == "e":
                        r, c = pos
                        newc = max(faces[5])[1]
                        newr = max(faces[5])[0] - (r - min(faces[2])[0])
                        newpos = (newr, newc)
                        print(pos, newpos, "e")
                        if newpos in blocked:
                            break
                        pos = newpos
                        d = "w"
                    if newpos[0] * newpos[1] < 0: exit(0)
                elif pos in faces[3]:
                    print(3)
                    if d == "e":
                        r, c = pos
                        newc = min(faces[2])[1] + (r - min(faces[3])[0])
                        newr = max(faces[2])[0]
                        newpos = (newr, newc)
                        if newpos in blocked:
                            break
                        pos = newpos
                        d = "n"
                        
                    elif d == "w":
                        r, c = pos
                        newc = min(faces[4])[1] + (r - min(faces[3])[0])
                        newr = min(faces[4])[0]
                        newpos = (newr, newc)
                        if newpos in blocked:
                            break
                        pos = newpos
                        d = "s"
                    if newpos[0] * newpos[1] < 0: exit(0)
                elif pos in faces[4]:
                    print(4)
                    if d == "n":
                        r, c = pos
                        newc = min(faces[3])[1]
                        newr = min(faces[3])[0] + (c - min(faces[4])[1])
                        newpos = (newr, newc)
                        if newpos in blocked:
                            break
                        pos = newpos
                        d = "e"
                    elif d == "w":
                        r, c = pos
                        newc = min(faces[1])[1]
                        newr = max(faces[1])[0] - (r - min(faces[4])[0])
                        newpos = (newr, newc)
                        if newpos in blocked:
                            break
                        pos = newpos
                        d = "e"
                    if newpos[0] * newpos[1] < 0: exit(0)
                elif pos in faces[5]:
                    print(5)
                    if d == "s":
                        r, c = pos
                        newc = max(faces[6])[1]
                        newr = min(faces[6])[0] + (c - min(faces[5])[1])
                        newpos = (newr, newc)
                        if newpos in blocked:
                            break
                        pos = newpos
                        d = "w"
                    elif d == "e":
                        r, c = pos
                        newc = max(faces[2])[1]
                        newr = max(faces[2])[0] - (r - min(faces[5])[0])
                        newpos = (newr, newc)
                        if newpos in blocked:
                            break
                        pos = newpos
                        d = "w"
                    if newpos[0] * newpos[1] < 0: exit(0)
                elif pos in faces[6]:
                    print(6)
                    if d == "e":
                        r, c = pos
                        newc = min(faces[5])[1] + (r - min(faces[6])[0])
                        newr = max(faces[5])[0]
                        newpos = (newr, newc)
                        if newpos in blocked:
                            break
                        pos = newpos
                        d = "n"
                    elif d == "s":
                        r, c = pos
                        newc = min(faces[2])[1] + (c - min(faces[6])[1])
                        newr = min(faces[2])[0]
                        newpos = (newr, newc)
                        if newpos in blocked:
                            break
                        pos = newpos
                        d = "s"
                    elif d == "w":
                        r, c = pos
                        newc = min(faces[1])[1] + (r - min(faces[6])[0])
                        newr = min(faces[1])[0]
                        newpos = (newr, newc)
                        if newpos in blocked:
                            break
                        pos = newpos
                        d = "s"
                    if newpos[0] * newpos[1] < 0: exit(0)
                    
                    
                        
                        
                
                        
                
                        
                # print("step", d,"at", pos, "to", newpos)
            
    if turn:
        # print("TURN", d, turn)
        d = change_dir(d, turn)
        # print("TO", d)
    

        
# print(pos, d)


dec = {"e": 0,"s": 1,"w": 2,"n": 3}
print(1000*pos[0] + 4*pos[1] + dec[d], d)
    
    



    
    
        
        
            
            
    
    
    



    
    
    

            
        
    
    

    


    



 





    


                


       
        


    
    
            
        

        
        
    