#tutorial on determining the summary statistics of a list of numbers
#below is the list to be filled by the user
numbers = [0]

while True:
    
    try:
        n = int(input("Enter a natural number (Enter a letter to stop): "))
        numbers.append(n)
    except ValueError:
        break

#calculate the mean of the numbers

s = sum(numbers)
N = len(numbers)

#mean
mean = s/N

print("The mean is ", mean)

#calculate the median of the numbers 
numbers.sort()
print(numbers)

if N%2 == 0:
    #Even number of data 
    mone = N/2
    mtwo = (N/2) + 1 
    #to read python list cast and shift 
    mone=int(mone)-1
    mtwo=int(mtwo)-1
    median = (numbers[mone]+numbers[mtwo])/2
else:
    #odd number of data
    m=(N+1)/2
    m=int(m)-1
    median=numbers[m]
print("The median is", median)

from collections import Counter
c= Counter(numbers)
mode = c.most_common(1)
Mode = mode[0][0]
print('The Mode is',Mode)

import math
#calculate the standard deviation 
y = 0
a=0
for x in numbers:
    y = (x-mean)**2
    a = a+y
    sigma = math.sqrt(a/N)
print ('The standard deviation is',sigma)