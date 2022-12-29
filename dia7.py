class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
        self.lvl = parent.lvl + 1 if parent else 0
        self.sons = []
        self.files = []
        
    
    def __eq__(self, o):
        return self.name == o.name and self.parent == o.parent
    
    def __str__(self):
        return self.name
    
    def calculate_size(self):
        self.size = sum(self.files) + sum([son.size for son in self.sons])
         
def main(lines):
    tree = []
    current_node = Node('/', None)
    tree.append(current_node)
    for line in lines:
        line = line.split()
        
        if line[0] == '$' and line[1] == 'cd': #COMMANDS
            if line[2] != '..':
                for son in current_node.sons:
                    if son.name == line[2]:
                        current_node = son
                        print('changing directory to', line[2])
                    
            else:
                current_node = current_node.parent
        elif line[0] != '$':
            if line[0] == 'dir':
                son = Node(line[1], current_node)
                current_node.sons.append(son)
                tree.append(son)
            else:
                current_node.files.append(int(line[0]))
    
    tree = sorted(tree, key = lambda x: x.lvl, reverse = True)
    for node in tree:
        node.calculate_size()
    
    total = 0
    for node in tree:
        if node.size <100000:
            total += node.size
        
    return tree, total

if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line[:-1] for line in file.readlines()]
    tree,total = main(lines)
    