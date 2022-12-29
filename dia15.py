import numpy as np
import re

mode = ['t.txt', 'input.txt']
file = mode[1]
lines  = open(file).read().splitlines()
lines = [list(map(int, re.findall(r"-*\d+", line))) for line in lines]

x = [l[0] for l in lines] + [l[2] for l in lines]
minx = int(min(x)*1.5)
maxx = int(max(x)*1.5)

class Sensor:
    def __init__(self, pos, closeb):
        self.pos = pos
        self.closeb = closeb
        self.man = abs(pos[0]-closeb[0])+ abs(pos[1]-closeb[1])
    
    def covered(self, point):
        return abs(self.pos[0]-point[0])+ abs(self.pos[1]-point[1]) <= self.man
    
    def points_covered(self, y_obj):
        self.points = set()
        x = self.pos[0]
        while self.covered((x, y_obj)):
            self.points.add(str((x, y_obj)))
            x+=1
        x = self.pos[0]   
        while self.covered((x, y_obj)):
            self.points.add(str((x, y_obj)))
            x-=1
        
                 
sensors = []
for line in lines:
    sensors.append(Sensor(line[:2], line[2:]))
    
total = 0
# result = ""
cov = False
y = 2000000

for sensor in sensors:
    sensor.points_covered(y)
    

sol = sensor.points
for sensor in sensors:
    sol = sol | sensor.points

beacons = set([str((line[2],line[3])) for line in lines if line[3] == y])

print(len(sol) -  len(beacons))
# print(minx, maxx)
# for x in range(minx, maxx+1):
#     # if x > (maxx+1-minx)*1.5:
#     #     print("1%")
#     #     break
#     for sensor in sensors:
#         if sensor.covered((x, y)):
#             # print((x, y), "covered by sensor:", sensor.pos, "dist", sensor.man)
#             cov = True
#             total+=1
#             break
#     # result+= "#" if cov else "." 
        
# print(total-1)
# # print(result)



 





    


                


       
        


    
    
            
        

        
        
    