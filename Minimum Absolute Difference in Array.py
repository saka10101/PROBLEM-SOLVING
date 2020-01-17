"""
Problem Title :Minimum Absolute Difference in an Array
Problem Statement: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
Coding language : python 3

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):


    '''
        #Approach 
        1.First sort the array and calculate the assumed smallest absolute difference(min_diff here) between two elements ie first and second elements
        2.Now loop over that sorted array without first two elements and check if the absolute difference is less than our initial assumption above.
           if yes repalce smallest absolute difference to new looped values 
        3.Finally return that smallest absolute difference value after loop completion

        here we sort array to get mostly min difference which is a greedy approach
    '''

    arr.sort()
    min_diff=abs(arr[0]-arr[1])
    for x in range(1,len(arr)-1):
        diff=abs(arr[x]-arr[x+1])
        if(min_diff>diff):
            min_diff=diff

    return min_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
