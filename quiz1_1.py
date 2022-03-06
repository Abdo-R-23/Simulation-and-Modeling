# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 16:25:05 2021

@author: Abdelrahman
"""
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def is_square(n):
    if n < 0:
         return 'negative'

    sq = math.floor(math.sqrt(n))
    if sq * sq == n:
         return True
    return False


def NumSqrs(x, y):
     sq = 0
     for i in range(x, y + 1):
         if is_square(i):
             print(i , "==")
             sq += 1
     print('\n')
     return sq


arrOfsqrs = []
for i in range(0, 10000, 1000):
     arrOfsqrs.append(NumSqrs(i, i + 1000))

plt.bar([str(i) + '_' + str(i + 1000) for i in range(0, 10000, 1000)], arrOfsqrs, width=1)
plt.show()
