# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 10:43:57 2021

@author: Abdelrahman
"""

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline 

mean = 2.5
std = 1.0
vals = np.random.normal(mean,std, size= 200)

vals.shape

plt.hist(vals)
