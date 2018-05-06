# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:00:10 2018

@author: Andrew Soth, Brian Pham, Preston Wong, Rayhaan Shaikh
"""

import random

print("------------------------Problem 1------------------------")
headProbability=float(input("Enter the probability of heads: "))
numberTrials=int(input("Enter the number of trials to simulate: "))
success = 0
fail = 0
for i in range(numberTrials):
    r = random.uniform(0,1)
    if r<headProbability:
        success = success + 1
        print("Success")
    else:
        fail = fail + 1
        print("Fail")

print("The number of Successes : ", success)
print("The number of Failures  : ", fail)


print("\n------------------------Problem 2------------------------")

pC =[.0001,.001,.001,.0001,.001]
pBC =[.9,.9,.9,.95,.95]
pBCFalse=[.001,.001,.01,.001,.01]

for i in range(len(pC)):
    probB = (pC[i]*pBC[i])+ pBCFalse[i]*(1-pC[i])
    answer = (pC[i]*pBC[i])/probB
    print("The probability of P(C|B) for row ",i+1," is: ",answer)











