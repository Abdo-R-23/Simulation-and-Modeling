# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 10:08:35 2021

@author: Abdelrahman
"""

# standard division (s.d) = 1 
# mean (u) = 0 
import numpy as np 
from matplotlib import pyplot as plt 
from scipy.stats import norm 
# Assigning the 100 points from -2 to 2 
data = np.linspace(-2,2,50)
"""
norm: is the object that help us to use .pdf method
norm.pdf : will give us the y value by substituting in the probability 
density function(PDF) with the mean = 0 and standard division = 1 
"""
# plotting 
plt.plot(data, norm.pdf(data,0,1))
plt.title("Normal distribution")
plt.xlabel("Values")
plt.ylabel("Density")
plt.show()