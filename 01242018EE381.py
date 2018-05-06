#
#
#
#
#Below is an implementation of the formula
#
#S(i + 1) = (M * S(i) + A) Mod N
#
#below are the values of the parameters used in the formula

#S = 1
M = 41
A = 31
N = 100

#below is a prompt for the user to enter the seed

S = int(input('Enter the value of your seed: '))

#below is the random number generator


for count in range(20):
    
    S = (M*S + A) % N


    #confine the randome numbers to the interval of 0-1

    r = S/N
    
    print(r)



