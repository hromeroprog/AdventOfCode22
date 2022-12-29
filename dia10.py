import numpy as np

mode = ['t.txt', 'input.txt']
file = mode[1]

X = 1
lines  = open(file).read().splitlines()

real = []
for line in lines:
    if line == 'noop':
        real.append(0)
    else:
        real.append(0)
        real.append(int(line.split()[1]))
       
interesting = [i for i in range(20,221,40)]
res = []
for cycle,val in enumerate(real):
    if cycle+1 in interesting:
        res.append(X*(cycle+1))
    X += val
        
    
print(sum(res))
    
    


            
        

        
        
    