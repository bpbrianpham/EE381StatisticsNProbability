# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 08:21:43 2018

@author: Brian
"""

import time

x = round(time.time() * 1000)

import numpy as np

a = np.matrix('2 3; 1 5')
b = np.matrix('1 4; -2 3')

print(a*b)

c = np.matrix('3 2; -1 0')

w, v = np.linalg.eig(c)

print("Lambda", w)
print("Vector", v)