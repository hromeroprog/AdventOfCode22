import numpy as np
import ast

mode = ['t.txt', 'input.txt']
file = mode[1]
lines  = open(file).read().splitlines()
lines = [[lines[i],lines[i+1]] for i in range(0, len(lines), 3)]


class Obj:
    def __init__(self, case: list):
        self.obj1 = case[0]
        self.obj2 = case[1]
        self.o1 = ast.literal_eval(self.obj1)
        self.o2 = ast.literal_eval(self.obj2)
        self.listas = [self.o1, self.o2]
        print("Caso", self.o1, "and", self.o2)
        self.x = self.same2(self.o1, self.o2)
        # self.x = self.same(self.o1, self.o2)
    
    def same2(self, lista1, lista2):
        if type(lista1) == list == type(lista2):
            maxlen = max(len(lista1), len(lista2))
            for i in range(maxlen):
                if i >= len(lista1):
                    return True
                if i >= len(lista2):
                    return False
                res = self.same2(lista1[i], lista2[i])
                if res is not None:
                    print('Catched result', res)
                    return res
      
        elif type(lista1) == list:
            return self.same2(lista1, [lista2])
        elif type(lista2) == list:
            return self.same2([lista1], lista2)
        else:
            if lista1 == lista2:
                print(f'Cont in {lista1}, {lista2}')
                return None
            if lista1 < lista2:
                print(f'True in {lista1}, {lista2}')
                return True
            if lista1 > lista2:
                print(f'False in {lista1}, {lista2}')
                return False
            
            
total = 0
for i,case in enumerate(lines):
    o = Obj(case)
    if o.x:
        print('True CASE #', i+1)
        total += i+1
    
    print(o.x)
print(total)



    


                


       
        


    
    
            
        

        
        
    