import numpy as np

if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line[:-1] for line in file.readlines()]
    visible_trees = set()
    grid = np.array([[int(tree) for tree in line] for line in lines])
    for x,line in enumerate(grid):
        mx = -1
        for y,tree in enumerate(line):
            if tree > mx:
                visible_trees.add(f'{x},{y}')
                mx = tree
                if mx == 9:
                    break
    for x,line in enumerate(grid):
        mx = -1
        for y,tree in enumerate(np.flip(line)):
            if tree > mx:
                visible_trees.add(f'{x},{len(line)-y-1}')
                mx = tree
                if mx == 9:
                    break
    for x,line in enumerate(grid.T):
        mx = -1
        for y,tree in enumerate(line):
            if tree > mx:
                visible_trees.add(f'{y},{x}')
                mx = tree
                if mx == 9:
                    break
    for x,line in enumerate(grid.T):
        mx = -1
        for y,tree in enumerate(np.flip(line)):
            if tree > mx:
                visible_trees.add(f'{len(line)-y-1},{x}')
                mx = tree
                if mx == 9:
                    break
    print(len(visible_trees))

        
        
    