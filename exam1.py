# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 08:06:23 2018

@author: Brian
"""

def mu(n,p):
    return n * p

def sigma(n,p):
    return math.sqrt(n * p * (1-p))

def z(x, mu, sigma):
    return ((x - mu) / sigma)

import random 
j = 0 

trials = 10000 # of repetitions 
N = 500 # given sample size  
x = 340 # success
p = 0.659 # probability of successes 

trial = [0] 
trial = trial * N 

for k in range (trials):
    for i in range(N): 
        r = random.uniform(0,1) 
        if r<p: 
            trial[i] = 1 #success 
        else: 
            trial[i] = 0 # failure
    s = sum(trial) # adds up total successes
    if s == x: 
        j = j + 1
  prob = j/trials 
    
  print('The probability is', prob)