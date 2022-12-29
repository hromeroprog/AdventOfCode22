import numpy as np

def calculate_score(tree_x, tree_y, grid):
    x = tree_x -1
    mx = grid[tree_y,tree_x]
    score = [0]*4
    while(x >= 0):
        score[0] += 1
        if grid[tree_y,x] >= mx:
            break
        x-=1
    x = tree_x + 1
    while(x < len(grid[tree_y])):
        score[1] += 1
        if grid[tree_y,x] >= mx:
            break
        x+= 1
    
    y = tree_y -1
    while(y >= 0):
        score[2] += 1
        if grid[y,tree_x] >= mx:
            break
        y-=1
    y = tree_y + 1
    while(y < len(grid[:,0])):
        score[3] += 1
        if grid[y,tree_x] >= mx:
            break
        y+= 1
    return np.array(score).prod()
    
    

if __name__ == '__main__':
    a  = open("input.txt").read().splitlines()
    b  = open("input.txt").read()
    c = open("input.txt").readlines()
    with open("input.txt") as file:
        lines = [line[:-1] for line in file.readlines()]
    visible_trees = set()
    grid = np.array([[int(tree) for tree in line] for line in lines])
    mx = -1
    for tree_y,line in enumerate(grid):
        for tree_x,tree in enumerate(line):
            score = calculate_score(tree_x, tree_y, grid)
            if score > mx:
                mx = score
            
        

        
        
    