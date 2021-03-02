#! /usr/bin/env python

"""
Author       : shiv

Description  :
"""

# Import statements
import random
import sys
import numpy as np
import time


startTime=time.time()

# Usage
usage = "Run the script like: python buttons_threads.py <number of buttons> <ratio of threads to buttons> <print or noprint>"

if len(sys.argv)!=4:
    print(usage)
    sys.exit(0)

print("********************************")
print("Starting a new experiment")
print("********************************")

# Reading the arguments and getting number of buttons and threads
# number of buttons
b = int(sys.argv[1])

# number of threads
ratio=float(sys.argv[2])
t = int(b*ratio)

# print details or not (print/noprint)
logs=sys.argv[3]

# Creating the original array
arr=[]
for i in range(b):
    arr.append(i)

array=np.array(arr)

print("The number of buttons: " + str(b))
print("The number of threads: " + str(t))

if(logs=="print"):
    print("Original array is: ")
    print(array)
    print("")
else:
    print("Created the original array (not printing bc long)")
    print("")

print("Going through the iterations of joining")
print("")

# variable to track number of iterations
count=0
while count < t:
    first_random_int=random.randint(0, b-1)
    second_random_int=random.randint(0, b-1)

    first_number=array[first_random_int]
    second_number=array[second_random_int]

    if(logs=="print"):
        print("First random number is: " + str(first_number))
        print("Second random number is " + str(second_number))

    if(first_number==second_number):
        if(logs=="print"):
            print("Not counting this run")
            print("")
        continue
    elif(first_number > second_number):
        count=count+1
        np.putmask(array, array==first_number, second_number)
    elif(second_number > first_number):
        count=count+1
        np.putmask(array, array==second_number, first_number)
    else:
        print("Should never hit this section")

    if(logs=="print"):
        print(array)
        print("")


print("*************************************************")
print("FINAL RESULTS:")
print("*************************************************")
# Calcuating most frequently occurring element and its occurrence
max_repeating_element=np.argmax(np.bincount(array))
max_repeating_count=np.count_nonzero(array==max_repeating_element)
print("Most frequent element occurrence:")
print(max_repeating_element)
print("")
print("Number of times it occurs")
print(max_repeating_count)
print("")

percentage=float(float(max_repeating_count)/float(b))*100
print("% connected in biggest blob: " + str(percentage) + "%")
print("")

executionTime=(time.time()-startTime)
print('Execution time in seconds: ' + str(executionTime))
