# EE 381 Project 5
# Linear Relationship Between Two Random Variables
#Rayhaan Shaikh 
#Mark Tan 
#Andrew Soth 
#Brian Pham 
#Preston Wong

import math
import numpy as np
import matplotlib.pyplot as plt

n = 6 # 6 data pairs total 
men = [59.7,72.9,41.9,46.2,50.3,43.2]
women=[63.8,77.8,44.5,48.3,54.0,43.5]

summationX = sum(men)
summationY = sum(women)

exy = [0,0,0,0,0,0]
i=0
while i < len(men):
    #getting indices for exy
    exy[i] = men[i]*women[i]
    i=i + 1

print(exy)


menSquared=[0]*n
womenSquared = [0]*n
i=0
while i < 6:
    #making list for ex^2 and ey^2
    menSquared[i] = men[i]*men[i]		# ex^2
    womenSquared[i]=women[i]*women[i]	# ey^2
    i=i+1
    
summationWomenSquared =sum(womenSquared)
summationMenSquared = sum(menSquared)
summationMen = sum(men)
summationWomen = sum(women)

i = 0

topOfFraction = 6 * (sum(exy)) - (summationMen)*(summationWomen)
bottomOfFraction = math.sqrt((6 * (summationMenSquared) - ((summationX)**2)) * ( ( (6 * summationWomenSquared))-(summationY**2)))
r = topOfFraction/bottomOfFraction #answer is .997 so positive correlation 

#df time to find the c.v
#d,f = n -2 on beachboard project 5 post so go to 10 and then .05 from there 
cv = 1.812
tv = r * (math.sqrt((6-2)/(1-r**2))) #solving for tv with the formula on beach board 
print ("The tv is",tv)

#reject null hypothesis since cv has been crossed 
#solving for a and b with the formulas posted on beachboard 
a= ((summationWomen*summationMenSquared) -(summationMen)*(sum(exy))) /(( 6*(summationMenSquared) - (summationMen)**2))
b=((6 * sum(exy) - ((summationMen) * (summationWomen)) ))  / ((6 * summationMenSquared) - summationMen**2)

# make scattered plot
plt.scatter(men, women)

#make regression line
f = np.array(range(40,75))
g = a + b * f
plt.plot(f,g)

#display graph with points and regression line
plt.title('Life Expectancy')
plt.xlabel('Men')
plt.ylabel('Women')
plt.show()

#predict new values of dependent variable (women) 
test_vals = [75,80,85,90] 
i = 0 
while i < len(test_vals): 
    g = a + b * test_vals[i] 
    print(test_vals[i]," ",g) 
    i += 1