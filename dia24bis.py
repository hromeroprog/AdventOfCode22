import numpy as np
import re
from sys import exit
import time

    
class Node:
    def __init__(self, pos,parent = None):
        self.parent = parent
        self.lvl = 0 if not parent else parent.lvl+1
        self.pos = pos
        # self.sons = []
    
    
mode = ['t24.txt', 'input24.txt']
file = mode[1]
lines  = open(file).read().splitlines()

st = (-1, 0)
down = set()
up = set()
left = set()
right = set()

maxc = len(lines[1]) - 3
maxr = len(lines) - 3

end = (maxr+1, maxc)


for r,line in enumerate(lines[1:-1]):
    for c,char in enumerate(line[1:-1]):
        if char == '>':
            right.add((r, c))
        elif char == '<':
            left.add((r, c))
        elif char == 'v':
            down.add((r, c))
        elif char == '^':
            up.add((r, c))

storms = {0:[down,up,left,right]}

queue = [Node(st)]
calculated = set()
start = time.time()
while queue:
    n = queue.pop(0)
    calculated.add((n.lvl, n.pos))
    if n.lvl+1 in storms:
        curr_storms = storms[n.lvl+1][0] | storms[n.lvl+1][1] | storms[n.lvl+1][2] | storms[n.lvl+1][3]
    else:
        print("Calculating storms of step", n.lvl +1)
        curr_storms = storms[n.lvl]
        ####
        ndown = set()
        for s in curr_storms[0]:
            new = (s[0] + 1, s[1])
            if s[0] + 1 > maxr:
                new = (0, s[1])
            ndown.add(new)
        
        nup = set()
        for s in curr_storms[1]:
            new = (s[0] - 1, s[1])
            if s[0] - 1 < 0:
                new = (maxr, s[1])
            nup.add(new)
            
        nleft = set()
        for s in curr_storms[2]:
            new = (s[0], s[1] -1)
            if s[1] - 1 < 0:
                new = (s[0], maxc)
            nleft.add(new)
            
        nright = set()
        for s in curr_storms[3]:
            new = (s[0], s[1] +1)
            if s[1] + 1 > maxc:
                new = (s[0], 0)
            nright.add(new)
            
        storms[n.lvl+1] = [ndown,nup,nleft,nright]
        curr_storms = storms[n.lvl+1][0] | storms[n.lvl+1][1] | storms[n.lvl+1][2] | storms[n.lvl+1][3]
      
    newpositions = set()
    newpositions.add(n.pos)
    newpos = (n.pos[0]+1, n.pos[1])
    if newpos == end:
        print("LVL", n.lvl + 1, newpos, "from", n.pos)
        end_node = Node(newpos, n)
        break
    if newpos[0] <= maxr or newpos == end:
        newpositions.add(newpos)
    
    newpos = (n.pos[0]-1, n.pos[1])    
    if newpos[0] >= 0 or newpos == st:
        newpositions.add(newpos)
    
    newpos = (n.pos[0], n.pos[1]+1)     
    if newpos[1] <= maxc:
        newpositions.add(newpos)
    
    newpos = (n.pos[0], n.pos[1]-1)     
    if newpos[1] >= 0:
        newpositions.add(newpos)
    
    if n.pos == st:
        newpositions = set()
        newpositions.add(n.pos)
        newpositions.add((n.pos[0] +1, n.pos[1]))
    newpositions = newpositions - curr_storms
    # print("NEW", newpositions)
    for pos in newpositions:
        son = Node(pos, n)
        if (son.lvl, son.pos) not in calculated:
            # n.sons.append(son.pos)
            queue.append(son)
            calculated.add((son.lvl, son.pos))

queue = [end_node]
calculated = set()
start = time.time()
while queue:
    n = queue.pop(0)
    calculated.add((n.lvl, n.pos))
    if n.lvl+1 in storms:
        curr_storms = storms[n.lvl+1][0] | storms[n.lvl+1][1] | storms[n.lvl+1][2] | storms[n.lvl+1][3]
    else:
        print("Calculating storms of step", n.lvl +1)
        curr_storms = storms[n.lvl]
        ####
        ndown = set()
        for s in curr_storms[0]:
            new = (s[0] + 1, s[1])
            if s[0] + 1 > maxr:
                new = (0, s[1])
            ndown.add(new)
        
        nup = set()
        for s in curr_storms[1]:
            new = (s[0] - 1, s[1])
            if s[0] - 1 < 0:
                new = (maxr, s[1])
            nup.add(new)
            
        nleft = set()
        for s in curr_storms[2]:
            new = (s[0], s[1] -1)
            if s[1] - 1 < 0:
                new = (s[0], maxc)
            nleft.add(new)
            
        nright = set()
        for s in curr_storms[3]:
            new = (s[0], s[1] +1)
            if s[1] + 1 > maxc:
                new = (s[0], 0)
            nright.add(new)
            
        storms[n.lvl+1] = [ndown,nup,nleft,nright]
        curr_storms = storms[n.lvl+1][0] | storms[n.lvl+1][1] | storms[n.lvl+1][2] | storms[n.lvl+1][3]
      
    newpositions = set()
    newpositions.add(n.pos)
    
    newpos = (n.pos[0]+1, n.pos[1])
    if newpos[0] <= maxr or newpos == end:
        newpositions.add(newpos)
    
    newpos = (n.pos[0]-1, n.pos[1])
    if newpos == st:
        print("LVL", n.lvl + 1, newpos, "from", n.pos)
        end_node = Node(newpos, n)
        break
    if newpos[0] >= 0 or newpos == st:
        newpositions.add(newpos)
    
    newpos = (n.pos[0], n.pos[1]+1)     
    if newpos[1] <= maxc:
        newpositions.add(newpos)
    
    newpos = (n.pos[0], n.pos[1]-1)     
    if newpos[1] >= 0:
        newpositions.add(newpos)
    
    if n.pos == end:
        newpositions = set()
        newpositions.add(n.pos)
        newpositions.add((n.pos[0] -1, n.pos[1]))
    newpositions = newpositions - curr_storms
    # print("NEW", newpositions)
    for pos in newpositions:
        son = Node(pos, n)
        if (son.lvl, son.pos) not in calculated:
            # n.sons.append(son.pos)
            queue.append(son)
            calculated.add((son.lvl, son.pos))
            
        

queue = [end_node]
calculated = set()
start = time.time()
while queue:
    n = queue.pop(0)
    calculated.add((n.lvl, n.pos))
    if n.lvl+1 in storms:
        curr_storms = storms[n.lvl+1][0] | storms[n.lvl+1][1] | storms[n.lvl+1][2] | storms[n.lvl+1][3]
    else:
        print("Calculating storms of step", n.lvl +1)
        curr_storms = storms[n.lvl]
        ####
        ndown = set()
        for s in curr_storms[0]:
            new = (s[0] + 1, s[1])
            if s[0] + 1 > maxr:
                new = (0, s[1])
            ndown.add(new)
        
        nup = set()
        for s in curr_storms[1]:
            new = (s[0] - 1, s[1])
            if s[0] - 1 < 0:
                new = (maxr, s[1])
            nup.add(new)
            
        nleft = set()
        for s in curr_storms[2]:
            new = (s[0], s[1] -1)
            if s[1] - 1 < 0:
                new = (s[0], maxc)
            nleft.add(new)
            
        nright = set()
        for s in curr_storms[3]:
            new = (s[0], s[1] +1)
            if s[1] + 1 > maxc:
                new = (s[0], 0)
            nright.add(new)
            
        storms[n.lvl+1] = [ndown,nup,nleft,nright]
        curr_storms = storms[n.lvl+1][0] | storms[n.lvl+1][1] | storms[n.lvl+1][2] | storms[n.lvl+1][3]
      
    newpositions = set()
    newpositions.add(n.pos)
    newpos = (n.pos[0]+1, n.pos[1])
    if newpos == end:
        print("LVL", n.lvl + 1, newpos, "from", n.pos)
        end_node = Node(newpos, n)
        break
    if newpos[0] <= maxr or newpos == end:
        newpositions.add(newpos)
    
    newpos = (n.pos[0]-1, n.pos[1])    
    if newpos[0] >= 0 or newpos == st:
        newpositions.add(newpos)
    
    newpos = (n.pos[0], n.pos[1]+1)     
    if newpos[1] <= maxc:
        newpositions.add(newpos)
    
    newpos = (n.pos[0], n.pos[1]-1)     
    if newpos[1] >= 0:
        newpositions.add(newpos)
    
    if n.pos == st:
        newpositions = set()
        newpositions.add(n.pos)
        newpositions.add((n.pos[0] +1, n.pos[1]))
    newpositions = newpositions - curr_storms
    # print("NEW", newpositions)
    for pos in newpositions:
        son = Node(pos, n)
        if (son.lvl, son.pos) not in calculated:
            # n.sons.append(son.pos)
            queue.append(son)
            calculated.add((son.lvl, son.pos))
    
print(time.time() - start, "segundos")   
    
    
    

    
        
    


    
    
        
        
            
            
    
    
    



    
    
    

            
        
    
    

    


    



 





    


                


       
        


    
    
            
        

        
        
    