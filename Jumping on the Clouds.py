"""
Problem Title :Drawing Book
Problem Statement: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
Coding language : python 3

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

#Thoughts:
#here we start with simple tracker approach to track the current state of game (ie its position and jumps with the following variable below)

    start_index=0
    stop_index=len(c)-1
    current_index=start_index
    jumps=0
    while(current_index != stop_index):  #ie tracking upto end
        if(current_index+1 != stop_index):   #ie tracking positions before second last cloud position is reached .Here jump over two clouds is possible as below..
            if(c[current_index+1]==1 ):
                current_index+=2
                jumps+=1
                           
            elif(c[current_index+2]==0):
                current_index+=2
                jumps+=1
            
            elif(c[current_index+2]==1):
                current_index+=1
                jumps+=1
            
        else: #ie when at the second last position ,possible jump as below..
            if(c[current_index+1]==0):
                current_index+=1
                jumps+=1



    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
