

#sum of sizes of directories of less than 100_000

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
         
        
class Tree:
    def __init__(self):
        self.tree = []


def main(lines):
    tree = []
    current_node = Node('/', None)
    tree.append(current_node)
    for line in lines:
        line = line.split()
        
        if line[0] == '$' and line[1] == 'cd': #COMMANDS
            if line[2] != '..':
                print(f'cd to {line[2]} from {current_node} with sons {[n.name for n in current_node.sons]}')
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
                print('Inserted son', son.name, 'at', current_node.name)
            else:
                current_node.files.append(int(line[0]))
    
    tree = sorted(tree, key = lambda x: x.lvl, reverse = True)
    for node in tree:
        node.calculate_size()
    
    tree = sorted(tree, key = lambda x: x.size)
    tot_disk = 70_000_000
    needed = 30000000
    
    total = 0
    for node in tree:
        if node.name == '/':
            total = node.size
    used = total
    print('total', total)
    tofree = needed - (tot_disk - used)
    print('Tof free', tofree)
    for node in tree:
        if node.size > tofree:
            print(node.size)
            break
        
            
    return tree, total
    
                
            
                        
                        

if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line[:-1] for line in file.readlines()]
    tree = main(lines)
    