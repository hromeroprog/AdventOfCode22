import numpy as np
import re
from sys import exit

class Monke:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.s1 = self.s2 = self.op = self.res = None
    
    def parse_desc(self, monkes):
        desc = self.desc.split(' ')
        if len(desc) == 1:
            self.res = int(desc[0])
        else:
            self.s1 = monkes[desc[0]]
            self.s2 = monkes[desc[2]]
            self.op = desc[1]
    
    def compute(self):
        if self.res != None:
            return self.res
        if self.op == '+':
            self.res = self.s1.compute() + self.s2.compute()
            return self.res
        if self.op == '-':
            self.res = self.s1.compute() - self.s2.compute()
            return self.res
        if self.op == '*':
            self.res = self.s1.compute() * self.s2.compute()
            return self.res
        if self.op == '/':
            self.res = self.s1.compute() / self.s2.compute()
            return self.res
    

mode = ['t21.txt', 'input21.txt']
file = mode[1]
lines  = list(map(lambda x: x.split(': '), open(file).read().splitlines()))


# x = [name for line in lines for name,op in line.split(': ')]
monkes = {m[0]:Monke(m[0], m[1]) for m in lines}

tree = [monkes['root']]
proc = []

while tree:
    m = tree.pop(0)
    proc.append(m)
    m.parse_desc(monkes)
    if m.s1:
        tree.append(m.s1)
        tree.append(m.s2)


print(monkes['root'].compute())



    



    
    
        
        
            
            
    
    
    



    
    
    

            
        
    
    

    


    



 





    


                


       
        


    
    
            
        

        
        
    