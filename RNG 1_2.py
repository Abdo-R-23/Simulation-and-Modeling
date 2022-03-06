# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 17:54:12 2021

@author: Abdelrahman
"""
"""
task in Random Number Generator name (RNG 1_2) 
the Second task makr ganert 16 number random and Uniform Distribution this number 
"""

import numpy as np
import matplotlib.pyplot as plt
seed=5
a=5
c=3
m=16

def seedLCG(initVal):
    global rand
    rand = initVal

def lcg1(seed,a,c,m):
    list1 =[]
    for i in range(0,m-1):
        seed =(a*seed+c)%m
        list1.append(seed)
    return list1

list =lcg1(seed,a,c,m)
print(list)


list3=[]
for seed2 in range(0,500):
    list4=lcg1(seed2,a,c,m)
    for seed3 in range(0,8):
        list3.append(list4[seed3])
plt.hist(list3,16,color='red')
plt.show


list5=[]
for seed5 in range(0,500):
    list6=lcg1(np.random.randint(50),a,c,m)
    for seed6 in range(0,8):
        list5.append(list6[seed6])
plt.hist(list5,16)
plt.show