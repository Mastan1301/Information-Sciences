#Exercise 1.6
#Use Python3 to run the program

import matplotlib.pyplot as plt

a = [chr(i) for i in range(ord('a'), ord('z') + 1)]

def mapping(x): #returns the index value corresponding to the letter in the alphabet
    return a.index(x)

f = open("eng.txt", 'r')
arr = [0 for i in range(0, 26)] #list for storing the count of each letter
total_count = 0
for i in f.read():
    if ord('a') <= ord(i) <= ord('z'): #checking if the character is from the alphabet
        arr[mapping(i)] += 1
        total_count += 1

p_arr = [i/total_count for i in arr] #computing the probability
print(p_arr)

    