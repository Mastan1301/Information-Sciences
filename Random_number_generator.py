#Exercise 1.4
#Use Python3 to run the program
#   Generating discrete random numbers using Inverse transform sampling method and plotting the CDF, Inverse CDF 
#   for the given PMF. The used PMF is arbitrary and can be changed to any type of PMF.

import numpy as np
import math
import matplotlib.pyplot as plt

val = [0, 1, 2, 3]
pmf = [0.1, 0.3, 0.1, 0.5]

def gen_random(set):
    return math.floor(set[0])


def gen_cdf(x): #function to generate CDF F_X(x)
    if(x < 0):
         return 0
    elif(x > 3):
         return 1
    else:
        cdf = 0
        for i in range(0, math.ceil(x)+1):
            cdf = cdf+pmf[i]
        return cdf

def inv_cdf(u, cdf): #quantile function
    i = 0
    while i < len(cdf)-1 and u > cdf[i]:
        i += 1

    if(i == len(val)-1):
        temp = 4
    else:
        temp = val[i+1]

    res = np.linspace(val[i], temp, 10) #a set of values corresponding to a particular 'u'

    return res 


num_trials = 10
u = np.random.uniform(low = 0, high = 1, size = num_trials) #generating independent uniformly random numbers in [0, 1]
cdf = [gen_cdf(i) for i in val]
x = []
for i in range(num_trials):
    x.append(gen_random(inv_cdf(u[i], cdf)))

print(x)

inv = [inv_cdf(j, cdf) for j in cdf]
print(inv)

#Plotting CDF
x1 = np.linspace(-5, 10, 1000)
cdf1 = np.zeros((len(x1)))
for i in range(len(x1)):
    cdf1[i] = gen_cdf(x1[i])

plt.plot(x1, cdf1)
plt.xlabel('x')
plt.ylabel('$F_X(x)$')
plt.title('CDF')
plt.savefig('cdf.jpg')
plt.grid()
plt.show()

#Plotting inverse of the CDF
u1 = np.linspace(0, 1, 1000)
icdf1 = np.zeros((len(u1)))
for i in range(len(u1)):
    icdf1[i] = gen_random(inv_cdf(u1[i], cdf))

plt.plot(u1, icdf1)
plt.xlabel('u')
plt.ylabel('$F_X^{-1}(u)$')
plt.title('Inverse of CDF')
plt.savefig('inv_cdf.jpg')
plt.grid()
plt.show()

# Testing: The following (commented) code is for verifying the random number generator. 
# If the PMF of x is approximately equal to the given PMF, then the program is correct. 
# Change num_trial's value to a large number, say 10000.

'''p = [x.count(i) for i in val]
for i in val:
    print(p[i]/sum(p)) #printing the pmf of x'''

    


    
