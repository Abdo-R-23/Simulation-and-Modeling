# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 17:07:17 2021

@author: Abdelrahman
"""
import numpy
import math
import matplotlib.pyplot as plt
import scipy.stats
#import Norm

def prime(n):
    for i in range (2,math.floor(math.sqrt(n) + 1)):
        if(n%i == 0 ): return False
    return True


def primerange(x,y):
    counter = 0
    for i in range(x,y+1):
        if prime(i):
            counter += 1
    return counter        
    
arr =[]
for i in range (1,1001,100):
    arr.append(primerange(i, i+100))
print(arr)


plt.bar([str(i)+ '-' +str(i+99) for i in range (1,1001,100)],arr,width=1)

plt.show()

            
        
        