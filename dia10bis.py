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
        
      
# interesting = [i for i in range(20,221,40)]
res = ""
for pix_pos,val in enumerate(real):
    if pix_pos %40 == 0:
        res+= "\n"
    if abs(pix_pos%40 - X) <= 1:
        res += "#"
    else:
        res += "."
    X += val
        
    
print(res)
    
    


            
        

        
        
    