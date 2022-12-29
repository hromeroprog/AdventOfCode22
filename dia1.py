# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:53:32 2022

@author: romer
"""
print(max(list(map(lambda x: sum([int(i) for i in x.split(',')]),','.join(list(map(lambda x: str(x[:-1]) if x!= '\n' else "-",open("input.txt", 'r').readlines()))).split(",-,")))))
    
    
    
