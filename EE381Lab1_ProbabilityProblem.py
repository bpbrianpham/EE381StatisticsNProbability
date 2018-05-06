# Probability problem 
import math 

N = 100000 # norm 
A = 4857 # adder 
M = 8601 #multiplier 
S = 0
Sum = 0 # initialize counter 
#trial = [] # number of trials 
trial = 0

Can = [0,0,0] 
K = int(input('Enter the number of experiments . ')) 

for k in range(K): # Outer loop
    #S = (2 * k) + k # seed 
    for i in range(3): 
        S = (M * S + A) % N
        r = S/N # The random number on [0,1)
        
        Can_Number = math.floor(r * 5 + 1) 
        Can[i] = Can_Number

    if ((Can[0] != Can[1]) & (Can[1] != Can[2]) & (Can[0] != Can[2])):
        Sum = Sum + 1
    #trial.append(Can)
prob = Sum/K
print("The probability of the 3 balls being in different cans is ", prob)
#print(trial)

