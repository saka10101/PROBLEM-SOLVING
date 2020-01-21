#!/bin/python3


"""
Problem Title :Strings: Maximum Array Sum
Problem Statement: https://www.hackerrank.com/challenges/max-array-sum/problem
Coding language : python 3

"""
import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    '''
    #Approach
    #Note:Its well know thief problem in geeks for geeks with nice explanation of solving approach there https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
    1.Loop through all elements in array in one shot, we have to determine result from this one loop only ie O(n) complexity
    2.During the loop maintain two tricky tracker variables that are nothing but basically the(+ -)of elements we traverse
        incl=array[i]+excl
        excl=Max(incl,excl)
        
        initially we define these trackers as zero and update their values on traversal
        At final loop Max(incl,excl) gives out desired result ie the maximum sum of subset of non-adjacent elements in list. We can visualize these trackers are just tracking ,summing adjecent elements ,adjusting to max in a loop traversal,simple but amazing and dynamic too 

    '''
    incl = 0
    excl = 0
     
    for i in arr: 
	
        # Current max excluding i (No ternary in  
        # Python) 
        new_excl = max(incl,excl) 
         
        # Current max including i 
        incl = excl + i 
        excl = new_excl 
      
    # return max of incl and excl 
    return (max(incl,excl)) 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
