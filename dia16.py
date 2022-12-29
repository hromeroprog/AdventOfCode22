import numpy as np
import re
from sys import exit

class Valve:
    def __init__(self, flow, valves: list):
        self.id = valves[0]
        self.flow = flow[0]
        self.connects = valves[1:]
        self.open = False

mode = ['t.txt', 'input.txt']
file = mode[1]
lines  = open(file).read().splitlines()
pattern = re.compile("[A-Z]{2}")
flows = [list(map(int, re.findall(r"-*\d+", line))) for line in lines]
valves = [pattern.findall(line) for line in lines]

vd = {}
for v,flow in zip(valves,flows):
    valve = Valve(flow,v)
    vd[v[0]] = valve
    
    

class Node:
    def __init__(self, parent ,at):
        self.at = at
        self.release = 0 if not parent else parent.release
        self.min = 0 if not parent else parent.min +1
        self.log = "" if not parent else parent.log
        self.open = {i:0 for i in vd} if not parent else parent.open.copy()
    
    def __eq__(self, o):
        return self.at == o.at and all(self.open[i]==o.open[i] for i in self.open) and self.release == o.release
    
    def ident(self):
        return (self.at, self.release)
        
        
st = "AA"

start = Node(None, st)
queue = [start]
trace = set()
finished = []
bag = set()
bag.add((st, 0))
to_open_valves = sum([1 for v in vd if vd[v].flow!=0])

while queue:
    n = queue.pop(0) 
    if n.min not in trace:
        print("Step", n.min)
        trace.add(n.min)
    if n.min == 30 or sum(n.open.values()) == to_open_valves:
        finished.append(n)
        continue

    for con in vd[n.at].connects:
        action = (con, n.release)
        # print(action)
        if action in bag:
            # print('Avoiding repeated action')
            continue
        
        son = Node(n, con)
        son.log += f"\nAt {n.at}, {son.min}: move to {son.at}"
        # if son not in queue:
        queue.append(son)
        bag.add(action)
    if vd[n.at].flow and not n.open[n.at]:
        son = Node(n, n.at)
        son.open[n.at] = 1
        son.log += f"\n{son.min}:open {n.at} will relase {(30-son.min)* vd[n.at].flow}"
        son.release = n.release + (30-son.min)* vd[n.at].flow
        bag.add((son.at, son.release))
        queue.append(son)
    # queue1 = sorted(queue, key = lambda x: x.min)[:50]
    # queue.sort(key = lambda x: x.release, reverse = True)
    # queue = queue1 + queue[:50]
    # queue = queue
    # queue = queue1
        # sons.append(Node())
queue = finished
q = max(queue, key = lambda x: x.release)
print(q.release, q.log)
#     sons = 
    
    

    


    



 





    


                


       
        


    
    
            
        

        
        
    