import numpy as np
import ast

class Scenario:
    def __init__(self, paths):
        x = [item[0] for sublist in paths for item in sublist]
        y = [item[1] for sublist in paths for item in sublist]
        maxx = max(x) +3
        minx = min(x) -3
        self.maxy = max(y) + 2
        self.offset = minx
        scenario = [['.' for i in range(minx, maxx)]for j in range(self.maxy)]
        scenario[0][500-self.offset] = '+'
        self.scenario = scenario
        self.paths = self.applyOffset(paths)
        self.start = [0, 500-self.offset]
        self.applyPaths()
        self.mapa()
        i = 0
        while self.drop_sand() != 'dropped':
            i+=1
            self.mapa()
        print('Needed: ', i)
            
        
    
        
    def drop_sand(self):
        row = self.start[0]
        col = self.start[1]
        while True:
            if row+1 >= len(self.scenario):
                print('dropped')
                return 'dropped'
            newpos = [row+1,col]
            obs = self.scenario[newpos[0]][newpos[1]]
            if obs in '#O':
                newpos = [row+1,col-1]
                obs = self.scenario[newpos[0]][newpos[1]]
                if obs in '#O':
                    newpos = [row+1,col+1]
                    obs = self.scenario[newpos[0]][newpos[1]]
                    if obs in '#O':
                        self.scenario[row][col] = 'O'
                        break
                    else:
                        row += 1
                        col += 1
                else:
                    row+=1
                    col-=1
            else:
                row+=1
        
        
    def mapa(self):
        self.map = '\n'.join([''.join(row) for row in self.scenario])
        print(self.map)
        
    def applyOffset(self, paths):
        for i in range(len(paths)):
            path = paths[i]
            for j in range(len(path)):
                paths[i][j][0] -= self.offset
        return paths
    
    def applyPaths(self):
        for path in self.paths:
            for i in range(len(path)-1):
                c1,r1 = path[i]
                c2,r2 = path[i+1]
                if c1 == c2:
                    if r1 < r2:
                        for r in range(r1, r2 +1):
                            self.scenario[r][c1] = '#'
                    else:
                        for r in range(r2, r1 +1):
                            self.scenario[r][c1] = '#'
                else:
                    if c1 < c2:
                        for c in range(c1, c2 +1):
                            self.scenario[r1][c] = '#'
                    else:
                        for c in range(c2, c1 +1):
                            self.scenario[r1][c] = '#'
                    
                        
                    
                
                
                
    
        
mode = ['t.txt', 'input.txt']
file = mode[1]
lines  = open(file).read().splitlines()
paths = [line.split(' -> ') for line in lines]
for i in range(len(paths)):
    path = paths[i]
    newpath = []
    for coords in path:
        intcoord = list(map(int, coords.split(',')))
        newpath.append(intcoord)
    paths[i] = newpath

s = Scenario(paths)




 





    


                


       
        


    
    
            
        

        
        
    