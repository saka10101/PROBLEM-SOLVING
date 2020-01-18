"""
Problem Title :Ice Cream Parlor
Problem Statement: https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem
Coding language : python 3

"""


#!/bin/python3

import math
import os
import random
import re
import sys


def findTwoCandidates(costs,budget): 
      
    # sort the array 
    A=sorted(costs)
    l = 0
    r = len(A)-1
      
    # traverse the array for the two elements and return when sum to budget 
    while l<r: 
        if (A[l] + A[r] == budget): 
            return [A[l],A[r]]
        elif (A[l] + A[r] < budget): 
            l += 1
        else: 
            r -= 1
    return 0

def whatFlavors(cost, money):
    '''
        #Approach:
        1.First using binary search way find two costs that sums to budget(here money) as shown in findTwoCandidates() func
        2.Now for two obtained costs find their respective ID's :
          Point to care:
          if both costs are of same value ... think what list.index(element) returns
          first find the index or ID (here index+1=ID) of a cost(here both cost same in this case)
          Then mutate the new value in this index and then find the index of that same valued cost again, you should get desired result
        

    '''

    nums=(findTwoCandidates(cost,money)) 
    if(cost.index(nums[0])<cost.index(nums[1])):
        if(nums[0]==nums[1]):
            b=cost.copy()
            f=b.index(nums[0])
            b[f]=-1
            print(str(str(f+1)+" "+str(b.index(nums[0])+1)))
    
        else:
            print(str(str(cost.index(nums[0])+1)+" "+str(cost.index(nums[1])+1)))
    else:
        if(nums[0]==nums[1]):
            b=cost.copy()
            f=b.index(nums[0])
            b[f]=-1
            print(str(str(f+1)+" "+str(b.index(nums[0])+1)))
        else:
            print(str(str(cost.index(nums[1])+1)+" "+str(cost.index(nums[0])+1)))



        




if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
