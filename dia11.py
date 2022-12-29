import numpy as np

mode = ['t.txt', 'input.txt']
file = mode[1]
lines  = open(file).read().split("\n\n")




class Monkey:
    def __init__(self, index, monkey_text):
        self.index = index
        self.text = monkey_text
        lines = self.text.splitlines()
        self.items = list(map(int, lines[1].split(":")[1][1:].split(', ')))
        self.update_func = lines[2].split("new = old ")[1][0]
        self.update_val = lines[2].split("new = old " + self.update_func+" ")[1]
        self.div = int(lines[3].split("by ")[1])
        self.true = int(lines[4].split("monkey ")[1])
        self.false = int(lines[5].split("monkey ")[1])
        self.inspected = 0
    
    def set_monkeys(self, monkey_list):
        self.monkey_list = monkey_list
    
    def turn(self):
        self.inspected += len(self.items)
        new_val = 0
        print("\n MONKEY TURN")
        for item in self.items:
            print(f"Monkey {self.index} inspecting {item}")
            if self.update_func == '*':
                if self.update_val == 'old':
                    new_val = item**2
                else:
                    new_val = item * int(self.update_val)
            elif self.update_func == '+':
                if self.update_val == 'old':
                    new_val = item*2
                else:
                    new_val = item + int(self.update_val)
            print(f"{item} increased to {new_val}")
            new_val = new_val//3
            print(f"divide 3: {new_val}")
            if new_val % self.div == 0:
                self.monkey_list[self.true].items.append(new_val)
            else:
                self.monkey_list[self.false].items.append(new_val)
        self.items = []
    
    def __str__(self):
        return f"Monkey {self.index} holding {self.items} inspected: {self.inspected}"
        
    
    
monkeys = []
for index, monkey_text in enumerate(lines):
    monkeys.append(Monkey(index, monkey_text))

for monkey in monkeys:
    monkey.set_monkeys(monkeys)


for m in monkeys:
    print(m)

print("run")

rounds = 20
for r in range(rounds):
    for monkey in monkeys:
        monkey.turn()

monkeys = sorted(monkeys, key = lambda x: x.inspected, reverse = True)
for m in monkeys:
    print(m)
    
m1, m2 = monkeys[:2]
print(m1.inspected * m2.inspected)
    
    
    
            
        

        
        
    