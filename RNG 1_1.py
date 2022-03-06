# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:24:16 2021

@author: Abdelrahman

"""
"""
task in Random Number Generator the frist task makr ganert 16 number random
"""
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def seedLCG(initVal):
    global rand
    rand = initVal

def lcg1():
    a = 5
    c = 3
    m = 16
    global rand
    rand = (a*rand + c) % m
    return rand
seedLCG(1)
for i in range(16):
    print (lcg1())



plt.hist(lcg1(),1)
    
    
    
    
    

    
    