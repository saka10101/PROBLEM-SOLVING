#!/bin/python3

"""
Problem Title :Arrays Left Rotation
Problem Statement: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
Coding language : python 3

"""
import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    # #FIRST APPROACH: SIMPLE BRUTE FORCE 
    #just two loops and swaps didn't passed most test cases
    # for i in range(d):
    #     temp = a[0] 
    #     for i in range(len(a)-1): 
    #         a[i] = a[i + 1] 
    #     a[n-1] =temp
    #SECOND APPROACH: QUEST FOR OPTIMIZATION
    #use of pop and append ,no need of two loops
    for i in range(d):
        temp=a.pop(0)
        #tempa=tempa[1:] didn't passed one last test case
        #del a[0] doesn't as we need to store a[0]
        #print(a) test1
        a.append(temp)
        #print(a) test2

    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
