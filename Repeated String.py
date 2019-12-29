"""
Problem Title :Repeated String
Problem Statement: https://www.hackerrank.com/challenges/repeated-string/problem
Coding language : python 3

"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):


#Thoughts:
#here approach is simple , just find no of a's in s , 
# then find how many times s is repeated in length n and how many spaces are left there(ie spaces inside n after removing exactly repeated s lengths)
# finally count no of a's in those left spaces 
# variable are named easy to understand as below..
    m=n//len(s)
    no_of_a_in_s=0
    total_a=0
    for x in range(len(s)):
        if(s[x]=='a'):
            no_of_a_in_s+=1
    
    space_covered_by_exact_repeats=len(s)*m
    total_a=no_of_a_in_s*m
    extra_spaces_for_repetation=n-space_covered_by_exact_repeats
    for y in range(extra_spaces_for_repetation):
        if(s[y]=='a'):
            total_a+=1



    return total_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
