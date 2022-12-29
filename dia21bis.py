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
        if self.name == 'humn':
            self.res = f"humn"
            return self.res
        if self.res != None:
            return self.res
        if self.name == 'root':
            self.res = f"{self.s1.compute()} == {self.s2.compute()}"
            return self.res
        
        
            
        if self.op == '+':
            self.res = f"({self.s1.compute()} + {self.s2.compute()})"
            if "humn" not in self.res:
                self.res = eval(self.res)
            return self.res
        if self.op == '-':
            self.res = f"({self.s1.compute()} - {self.s2.compute()})"
            if "humn" not in self.res:
                self.res = eval(self.res)
            return self.res
        if self.op == '*':
            self.res = f"({self.s1.compute()} * {self.s2.compute()})"
            if "humn" not in self.res:
                self.res = eval(self.res)
            return self.res
        if self.op == '/':
            self.res = f"({self.s1.compute()} / {self.s2.compute()})"
            if "humn" not in self.res:
                self.res = eval(self.res)
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


humn = 7570725973817
res = monkes['root'].compute()
# print(res)
r1,r2 = res.split(' == ')
r2 = eval(r2)
# while not(eval(res)):
#     if humn % 100 == 0:
#         print(humn)
#     humn += 1
res = r1
r1 += f"-{r2}"

'''
Prints, encontrar recta y ver ordenada en el origen.

humn = -14560725974393.526

eval(r1)
Out[152]: 74219815739835.31

humn = -14500725974393.526

eval(r1)
Out[154]: 73973997558017.12

humn = -14300725974393.526

eval(r1)
Out[156]: 73154603618623.19

humn = 3555057453229.037

eval(r1)
Out[158]: -0.1533203125

humn = 3555057453229

eval(r1)
Out[160]: 0.0

'''
# for i in range(65):
#     res = res[1:-1]
    
#     print(i, "\n", res)
#     if res[0] == '(':
#         back = 0
#         while res[-back] != ')':
#             back += 1
#         back -= 1
#         end = res[-back:]
#         end = end.split()
#         res = res[:-back]
#         if end[0] == '+':
#             r2 -= eval(end[1])
#         if end[0] == '-':
#             r2 += eval(end[1])
#         if end[0] == '*':
#             r2 /= eval(end[1])
#         if end[0] == '/':
#             r2 *= eval(end[1])
#     elif res[-1] == ')':
#         front = 0
#         while res[front] != '(':
#             front += 1
#         front -= 1
#         end = res[:front]
#         end = end.split()
#         res = res[front+1:]
#         if end[1] == '+':
#             r2 -= eval(end[0])
#         if end[1] == '-':
#             r2 += eval(end[0])
#         if end[1] == '*':
#             r2 /= eval(end[0])
            
#         if end[1] == '/':
#             # r2 *= eval(end[1])
            
#             print('front div')
#             exit(0)

    
    



    
    
        
        
            
            
    
    
    



    
    
    

            
        
    
    

    


    



 





    


                


       
        


    
    
            
        

        
        
    