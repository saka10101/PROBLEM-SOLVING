
"""
Problem Title :Electronics Shop
Problem Statement: https://www.hackerrank.com/challenges/electronics-shop/problem
Coding language : python 3

"""

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):


    #Thoughts(The brute force approach):
    #first find prices sum combinations of two items 
    #check if its equal to budget ==>that's the much possible expenditure out of budget ie our goal to find
    #else find the maximum of the total sum combinations

    sum_value_options=[]
    for x in range(len(keyboards)):
        for y in range(len(drives)):

            sum_value=keyboards[x]+drives[y]
            if(sum_value<= b):
                if(sum_value == b):
                    return sum_value
                else:
                    sum_value_options.append(sum_value)
            
    if sum_value_options:
        return(max(sum_value_options))
    else:
        return -1

    
                

            


   
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
