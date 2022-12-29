import numpy as np

mode = ['t.txt', 'input.txt']
file = mode[1]

lines  = list(map(lambda x: [x.split()[0], int(x.split()[1])],open(file).read().splitlines()))

H,T = np.array((0, 0)),np.array((0, 0)), np.array((0, 0))

dx = {'U':np.array([0,1]), 'D':np.array([0,-1]), 'L':np.array([-1,0]), 'R':np.array([1,0])}
positions = {str(T)}
for d, num in lines:
    # print(d, num, "for head")
    for _ in range(num):
        H += dx[d]
        print('H', H)
        Tdist = H - T
        if abs(Tdist[0]) > 1 or abs(Tdist[1]) > 1:
            T += dx[d]
            Tdist = H - T
            if abs(Tdist[0]) == 1 and abs(Tdist[1]) == 1:
                if dx[d][0]:
                    T[1] = H[1]
                elif dx[d][1]:
                    T[0] = H[0]
                positions.add(str(T))
                # print('add', str(T), "with move diagonal",d, dx[d])
            else:
                positions.add(str(T))
                # print('add', str(T), "with move",d, dx[d])
                
print(len(positions))
    
    
    


            
        

        
        
    