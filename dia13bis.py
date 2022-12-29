import numpy as np
import ast

mode = ['t.txt', 'input.txt']
file = mode[1]
lines1  = open(file).read().splitlines()
lines = [lines1[i] for i in range(0, len(lines1)) if i%3 != 2]

# class Lista:
#     def __init__(self, case:str):
#         self.lista = ast.literal_eval(case)
    
#     def __eq__(self, o):
#         lista1 = self.lista
#         lista2 = o
#         if type(lista1) == list == type(lista2):
#             maxlen = max(len(lista1), len(lista2))
#             for i in range(maxlen):
#                 if i >= len(lista1):
#                     return True
#                 if i >= len(lista2):
#                     return False
#                 res = self.same2(lista1[i], lista2[i])
#                 if res is not None:
#                     print('Catched result', res)
#                     return res
      
#         elif type(lista1) == list:
#             return self.same2(lista1, [lista2])
#         elif type(lista2) == list:
#             return self.same2([lista1], lista2)
#         else:
#             if lista1 == lista2:
#                 print(f'Cont in {lista1}, {lista2}')
#                 return None
#             if lista1 < lista2:
#                 print(f'True in {lista1}, {lista2}')
#                 return True
#             if lista1 > lista2:
#                 print(f'False in {lista1}, {lista2}')
#                 return False
#     smaller 
def compare(lista1, lista2):
    # if ',' not in str(lista1):
    #     if ',' in str(lista2):
    #         return -1
    #     else:
    #         return len(str(lista1)) - len(str(lista2))
    
    # if ',' not in str(lista2):
    #     if ',' in str(lista1):
    #         return 1
    #     else:
    #         return len(str(lista2)) - len(str(lista1))
        
        
    if type(lista1) == list == type(lista2):
        maxlen = max(len(lista1), len(lista2))
        for i in range(maxlen):
            if i >= len(lista1):
                return -1
            if i >= len(lista2):
                return 1
            res = compare(lista1[i], lista2[i])
            if res is not None:
                # print('Catched result', res)
                return res
  
    elif type(lista1) == list:
        return compare(lista1, [lista2])
    elif type(lista2) == list:
        return compare([lista1], lista2)
    else:
        if lista1 == lista2:
            # print(f'Cont in {lista1}, {lista2}')
            return None
        if lista1 < lista2:
            # print(f'True in {lista1}, {lista2}')
            return -1
        if lista1 > lista2:
            # print(f'False in {lista1}, {lista2}')
            return 1

objects = list(map(ast.literal_eval, lines + ['[[2]]', '[[6]]']))


# for i in range()
from functools import cmp_to_key
for i in range(len(objects)):
    if str(objects[i]) == '[[2]]' or str(objects[i]) == '[[6]]':
        print(i+1)
        
a = sorted(objects, key=cmp_to_key(compare))
a = list(map(str, a))
vac = 0
for i in range(len(a)):
    if not any(char.isdigit() for char in a[i]):
        print("Vacios:", len(a) - i)
        vac = len(a) - i

for i in range(len(a)):
    if str(a[i]) == '[[2]]' or str(a[i]) == '[[6]]':
        print(i+1)

    

       
        


    
    
            
        

        
        
    