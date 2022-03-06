# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:29:44 2021

@author: Abdelrahman
"""
from random import randint
import matplotlib.pyplot as plt


def lcg(a, c, m,x):
        
    x0 = (a*x + c) % m
    return x


list = []


for i in range(16):
    if i>=8:
        x = randint(0,8)
    if i< 8:
        x=randint(8, 16)
    
        
   
    
    list.append(lcg(5,3,8,x))
   
    
plt.hist(list, 10, edgecolor='orange')



print (list)    