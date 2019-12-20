"""
Problem Title :Drawing Book
Problem Statement: https://www.hackerrank.com/challenges/drawing-book/problem
Coding language : python 3

"""

#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):

    if(n==1 or p==n): #ie no need to do calculation for this one(intutively)
        return 0

    #Here we utilize the integer division
    #first dividing(integer division) the total pages by 2 gives total turns required to reach the last page =>i in code below 
    #Then dividing (integer division)the target page by 2 gives total turns required to reach from front of book =>j in code below
    #difference [1]-[2] gives total turns required from the back of the book =>i-j in code below
    #so to reach target page we can do it by choosing minimum of j (starting from front of book) or i-j(starting from back of book)
    
    else:
        i=n//2
        j=p//2
        return min(j,i-j)
        





if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
