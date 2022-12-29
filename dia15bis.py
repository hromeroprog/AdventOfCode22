import numpy as np
import re

mode = ['t.txt', 'input.txt']
file = mode[0]
lines  = open(file).read().splitlines()
lines = [list(map(int, re.findall(r"-*\d+", line))) for line in lines]

# x = [l[0] for l in lines] + [l[2] for l in lines]
# maxy = maxx = 4000000
maxy = maxx = 20

class Sensor:
    def __init__(self, pos, closeb):
        self.pos = pos
        self.closeb = closeb
        self.man = abs(pos[0]-closeb[0])+ abs(pos[1]-closeb[1])
    
    def covered(self, point):
        return abs(self.pos[0]-point[0])+ abs(self.pos[1]-point[1]) <= self.man
    
    # def points_covered(self, maxx,maxy):
    #     self.points = set()
    #     x = self.pos[0]
    #     y = self.pos[1]
        
        if True:
            x = self.pos[0]
            y = self.pos[1]
            while x <= maxx and x <= self.pos[0] + self.man:
                while y <= maxy and y <= self.pos[1] + self.man:
                    if self.covered((x, y)):
                        self.points.add(str((x, y)))
                    y += 1
                y = self.pos[1]
                x+=1
            x = self.pos[0]
            y = self.pos[1]
            
            while x <= maxx and x <= self.pos[0] + self.man:
                while y >= 0 and y >= self.pos[1] - self.man:
                    if self.covered((x, y)):
                        self.points.add(str((x, y)))
                    y -= 1
                y = self.pos[1]
                x+=1
            x = self.pos[0]
            y = self.pos[1]
            
            while x >= 0 and x >= self.pos[0] - self.man:
                while y <= maxy and y <= self.pos[1] + self.man:
                    if self.covered((x, y)):
                        self.points.add(str((x, y)))
                    y += 1
                y = self.pos[1]
                x-=1
            x = self.pos[0]
            y = self.pos[1]
            while x >= 0 and x >= self.pos[0] - self.man:
                while y >= 0 and y >= self.pos[1] - self.man:
                    if self.covered((x, y)):
                        self.points.add(str((x, y)))
                    y -= 1
                y = self.pos[1]
                x-=1
            # x = self.pos[0]
            # y = self.pos[1]
            
            # while x <= maxx and x <= self.pos[0] + self.man:
            #     while y <= maxy and y <= self.pos[1] + self.man:
            #         if self.covered((x, y)):
            #             self.points.add(str((x, y)))
            #         y += 1
            #     x+=1
            # x = self.pos[0]
            # y = self.pos[1]
            # cond = True
            # while x >= 0 and cond1:
            #     cond2 = True
            #     while y <= maxy and cond2:
            #         if self.covered((x, y)):
            #             self.points.add(str((x, y)))
            #         else:
            #             cond2 = False
            #         y += 1
            #     x-=1
            # x = self.pos[0]
            # y = self.pos[1]
            # cond = True    
            # while x <= maxx and cond1:
            #     cond2 = True
            #     while y >= 0 and cond2:
            #         if self.covered((x, y)):
            #             self.points.add(str((x, y)))
            #         else:
            #             cond2 = False
            #         y -= 1
            #     x+=1
            # x = self.pos[0]
            # y = self.pos[1]
            # cond = True    
            # while x >= 0 and cond1:
            #     cond2 = True
            #     while y >= 0 and cond2:
            #         if self.covered((x, y)):
            #             self.points.add(str((x, y)))
            #         else:
            #             cond2 = False
            #         y -= 1
            #     x-=1
        # else:
        #     x = self.pos[0]
        #     y = self.pos[1]
        #     if x > maxx and x - self.man > maxx:
        #         while x >= 0:
        #             cond2 = True
        #             while y >= 0:
        #                 if self.covered((x, y)):
        #                     self.points.add(str((x, y)))
        #                 y -= 1
        #             x-=1
        #         x = self.pos[0]
        #         y = self.pos[1]
        #         while x >= 0:
        #             cond2 = True
        #             while y <= maxy:
        #                 if self.covered((x, y)):
        #                     self.points.add(str((x, y)))
        #                 y += 1
        #             x-=1
                    
                    
        #     x = self.pos[0]
        #     y = self.pos[1]
        #     if (x < 0 and  x + self.man > 0):
        #         while x <= maxx:
        #             cond2 = True
        #             while y >= 0:
        #                 if self.covered((x, y)):
        #                     self.points.add(str((x, y)))
        #                 y -= 1
        #             x+=1
        #         x = self.pos[0]
        #         y = self.pos[1]
        #         while x  <= maxx:
        #             cond2 = True
        #             while y <= maxy or y <= self.pos[1] + self.man:
        #                 if self.covered((x, y)):
        #                     self.points.add(str((x, y)))
        #                 y += 1
        #             x-=1
        #         x = self.pos[0]
        #         y = self.pos[1]
        #         while x >= 0:
        #             cond2 = True
        #             while y <= maxy or y >= 0:
        #                 if self.covered((x, y)):
        #                     self.points.add(str((x, y)))
        #                 y -= 1
        #             x-=1
                
                
            
        # x = self.pos[0]   
        # while self.covered((x, y_obj)):
        #     self.points.add(str((x, y_obj)))
        #     x-=1
        
        # for x in range(maxx+1):
        #     for y in range(maxy+1):
        #         if self.covered((x, y)):
        #             self.points.add(str((x, y)))
        
                 
sensors = []
for line in lines:
    sensors.append(Sensor(line[:2], line[2:]))
    
total = 0
# result = ""
# cov = False
# y = 2000000
for sensor in sensors:
    print('Evaluated sensor', len(sensors))
    sensor.points_covered(maxx,maxy)

points = set([str((x,y)) for x in range(maxx+1) for y in range(maxy+1)])
beacons = set([str((line[2],line[3])) for line in lines if (line[3]<=maxy and line[3] >= 0 and line[2]<=maxx and line[2] >= 0)])
    

sol = sensor.points
for sensor in sensors:
    sol = sol | sensor.points

point = points-sol

print(point)
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



 





    


                


       
        


    
    
            
        

        
        
    