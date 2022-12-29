# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:22:59 2022

@author: romer
"""

print(sum(sorted(list(map(lambda x: sum([int(i) for i in x.split(',')]),','.join(list(map(lambda x: str(x[:-1]) if x!= '\n' else "-",open("input.txt", 'r').readlines()))).split(",-,"))))[-3:]))
    
    
    
