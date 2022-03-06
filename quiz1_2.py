# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:00:57 2021

@author: Abdelrahman
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def is_div_sum(n):
    if n<0:
        return 'nag'
    div = math.floor(n)
    if div/div == n:
        return True
    return False
    