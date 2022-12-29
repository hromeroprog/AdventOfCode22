import numpy as np

mode = ['t.txt', 'input.txt']
file = mode[1]

lines  = list(map(lambda x: [x.split()[0], int(x.split()[1])],open(file).read().splitlines()))

knots = {i:np.array([0,0]) for i in range(10)}

dx = {'U':np.array([0,1]), 'D':np.array([0,-1]), 'L':np.array([-1,0]), 'R':np.array([1,0])}
positions = {str(knots[9])}
for d, num in lines:
    # print(d, num, "for head")
    for _ in range(num):
        knots[0] += dx[d]
        # print('new H', knots[0])
        for k in range(9):
            Tdist = knots[k] - knots[k+1]
            if abs(Tdist[0]) == 2 and abs(Tdist[1]) == 2:
                knots[k+1] += Tdist//2
                
            elif abs(Tdist[0]) == 2:
                if not Tdist[1]:
                    knots[k+1] += Tdist//2
                else:
                    knots[k+1][0] += Tdist[0]//2
                    knots[k+1][1] = knots[k][1]
            elif abs(Tdist[1]) == 2:
                if not Tdist[0]:
                    knots[k+1] += Tdist//2
                else:
                    knots[k+1][1] += Tdist[1]//2
                    knots[k+1][0] = knots[k][0]
            # print('knot',k+1,'at', knots[k+1])
            positions.add(str(knots[9]))
    # print(f'End of move: {[(p,list(knots[p])) for p in knots]}')
                
print(len(positions))
    
    
    


            
        

        
        
    