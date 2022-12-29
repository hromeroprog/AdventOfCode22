import numpy as np
import re

mode = ['t.txt', 'input.txt']
file = mode[1]
lines  = open(file).read().splitlines()
lines = [list(map(int, re.findall(r"-*\d+", line))) for line in lines]

maxy = maxx = 4000000
# maxy = maxx = 20

class Sensor:
    def __init__(self, pos, closeb):
        self.pos = pos
        self.closeb = closeb
        self.man = abs(pos[0]-closeb[0])+ abs(pos[1]-closeb[1])
    
    def covered(self, point):
        return abs(self.pos[0]-point[0])+ abs(self.pos[1]-point[1]) <= self.man
                 
sensors = []
for line in lines:
    sensors.append(Sensor(line[:2], line[2:]))

for y in range(maxy+1):
    # if y % (maxy//1000) == 0:
    #     print('1/30')
    if y % 1000 == 0:
        print(y)
    # print(y)
    x = -1
    while x <= maxx:
        x += 1
        jumped = False
        for sensor in sensors:
            if sensor.pos[0] + sensor.man > x and sensor.pos[0] - sensor.man < x and sensor.covered((x,y)):
                x = sensor.pos[0] + sensor.man - abs(sensor.pos[1] - y)
                jumped = True
                break
        if not jumped:
            print(x, y)
            break
                



 





    


                


       
        


    
    
            
        

        
        
    