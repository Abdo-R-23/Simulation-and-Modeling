# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:27:16 2021

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
    
def gp(l,w):    # i make generate probability 
                #this fun teken low and high
    return random.randint(l,w)

    
def ave_pueue(n):  #According to the waiting time after that the total waiting time then
                   #according std and mean 
                   
    time =[] #this time like a service 
    weittime = 0 #frist weit time 
    allweittim=0 #totel weit time 
    
    for i in range(n):
        if (gp(1,5) !=4): # from generate probability if  the result comes out, it is not equal 4
                          # Make continue 
                          # but the number 4 we help make probability can change
            continue
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
        
        
    
