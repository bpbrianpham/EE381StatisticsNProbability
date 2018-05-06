def RNG(M, A, N, seed, repitition):
    data = []
    m = M
    a = A
    n = N
    S = seed

    for count in range(repitition):
        
        S = (M * S + A) % N


        #confine the randome numbers to the interval of 0-1

        
        data.append(S/N)
        
    return data

def mean(data):    
    return (sum(data) / len(data))

def PrintRNG(data):
    for n in range(len(data)):
        print('{0:.4g}'.format(data[n]))

#Exercise 1
print("--------Exercise 1----------\n")
print("Seed = 0\n")
PrintRNG(RNG(6, 5, 11, 0, 20))
print("\n")
print("Seed = 4\n")
PrintRNG(RNG(6, 5, 11, 4, 20))


#Exercise 2
print("--------Exercise 2----------\n")
seeds = [0, 1, 4, 5]
for n in range(len(seeds)):
    print("\n*** Seed = ", seeds[n], "***")
    PrintRNG(RNG(6, 3, 7, seeds[n], 20))

print()
#Computer Program
print("--------Programming----------\n")


data = RNG(8601, 4857, 10000, 0, 100)

PrintRNG(data)

print("\nThe mean is ", '{0:.4g}'.format(mean(data)))






