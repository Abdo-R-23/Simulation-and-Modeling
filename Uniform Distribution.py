# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 10:11:33 2021

@author: Abdelrahman
"""

import numpy as np
import matplotlib.pyplot as plt

"""
np.random.uniform Draw samples from a uniform distribution and Returns out
((ndarray or scalar)) Drawn samples from the parameterized uniform distribution.
"""
data = np.random.uniform(0,1,500) # You are generating 500 points between 0 and 1.
plt.hist(data,20) 
##20 is the number of columns that will be draw 
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title("Uniform Distribution")
plt.axis([0, 1, 0, 30]) # x_start, x_end, y_start, y_end 
plt.show()