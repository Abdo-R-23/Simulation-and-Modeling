# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 10:25:16 2021

@author: Abdelrahman
"""
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np


x_min = 0.0
x_max = 16.0

mean = 8.0 
std = 2.0

x = np.linspace(x_min, x_max, 200)

y = scipy.stats.norm.pdf(x,mean,std)

plt.plot(x,y, color='coral')

plt.grid()

plt.xlim(x_min,x_max)
plt.ylim(0,0.25)

plt.title('How to plot a normal distribution in python with matplotlib',fontsize=10)

plt.xlabel('x')
plt.ylabel('Normal Distribution')

plt.savefig("normal_distribution.png")
plt.show()