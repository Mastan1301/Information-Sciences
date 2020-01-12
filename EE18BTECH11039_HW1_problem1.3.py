#Exercise 1.4
#Use Python3 to run the program

import numpy as np
import math

val = [0, 1]
p = 0.3 #say 
pmf = [1-p, p]

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
        
    res = np.linspace(val[i], temp, 100) #a set of values corresponding to a particular 'u'
    return res 

num_trials = 100
u = np.random.uniform(low = 0, high = 1, size = num_trials) #generating independent uniformly random numbers in [0, 1]
cdf = [gen_cdf(i) for i in val]
x = []
for i in range(num_trials):
    x.append(gen_random(inv_cdf(u[i], cdf)))

print(x)
# Testing: The following (commented) code is for verifying the random number generator. 
# If the PMF of x is approximately equal to the given PMF, then the program is correct. 
# For verifying the correctness of the program, change num_trial's value to a large number, say 10000.

'''p = [x.count(i) for i in val]
for i in val:
    print(p[i]/sum(p)) #printing the pmf of x'''

    


    