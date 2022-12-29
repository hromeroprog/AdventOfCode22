import numpy as np

mode = ['t.txt', 'input.txt']
file = mode[1]
lines  = np.array(open(file).read().splitlines())

class Node:
    def __init__(self, letter):
        self.start = False
        self.end = False
        self.height = ord(letter)
        self.adjacent = []
        self.prev = []

def createNodeMap(lines):
    nodes = []
    stnode = Node('a')
    enode = Node('z')
    for line in lines:
        nodeline = []
        for char in line:
            if char == 'S':
                stnode = Node('a')
                stnode.start = True
                nodeline.append(stnode)
            elif char == 'E':
                enode = Node('z')
                enode.end = True
                nodeline.append(enode)
            else:
                nodeline.append(Node(char))
        nodes.append(nodeline.copy())
    for row in range(len(nodes)):
        for col in range(len(nodes[row])):
            n = nodes[row][col]
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if abs(i) + abs(j) == 1:
                        # print(i, j)
                        r = row+ i
                        c = col + j
                        if r >= 0 and c >= 0 and r < len(nodes) and c < len(nodes[0]):
                            if nodes[r][c].height <= n.height +1:
                                n.adjacent.append(nodes[r][c])
                                nodes[r][c].prev.append(n)
    return stnode, enode, nodes

st,end,nodes = createNodeMap(lines)
evaluated = set()
st.lvl = 0
queue = [st]
n = 0
lvl = 0
while(True):
    n = queue.pop(0)
    if n.lvl > lvl:
        print('Evaluating new lvl', lvl)
        lvl = n.lvl
    
    
    if n.end:
        break
    if str(n) in evaluated:
        continue
    evaluated.add(str(n))
    for adj in n.adjacent:
        if str(adj) not in evaluated:
            adj.lvl = n.lvl + 1
            queue.append(adj)
            # evaluated.add(str(n))
                


       
        


    
    
            
        

        
        
    