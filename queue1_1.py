# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 16:34:03 2021

@author: Abdelrahman
"""

import random
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

queue = []    #create queue

def addinqueue(number):     #adding queue
    queue.append(number)
    
def popqueue():         #delete queue
    if (len(queue) == 0) : return
    queue.pop(0)
    

    
def ave_pueue(n):  #According to the waiting time after that the total waiting time then
                   #according std and mean 
                   
    time =[] #this time like a service 
    weittime = 0 #frist weit time 
    allweittim=0 #totel weit time 
    num = random.randint(1, 20) 
    time.append(num)
    weittime +=num
    allweittim += weittime
    addinqueue(num)
    for i in range(n):
        
        
        popqueue()
    return [allweittim /n , allweittim, np.std(time),np.mean(time)] #accroding ave totel weit time 
                                                                    #and allweit time , std and mean

print (ave_pueue(100))    #for 100 person 
        
        
    
