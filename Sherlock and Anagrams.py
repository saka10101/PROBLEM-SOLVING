"""
Problem Title : Sherlock and Anagrams
Problem Statement: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
Coding language : python 3

"""
#!/bin/python3

import math
import os
import random
import re
import sys
import collections
# Complete the sherlockAndAnagrams function below.

def combination(n,r):
    return int(math.factorial(n)/(math.factorial(n-math.factorial(2))*math.factorial(2)))
     
        
def sherlockAndAnagrams(s):

    '''
    Thoughts:
    1.First identify all possible substrings of a string using loopings and slicings
    2.Then sort that substring list
    3.Find out the elements in above list with same elements and store in dictionary:
      -first convert the list into tuples :(....you'll know later because list is an unhashable type)
      -Use custom code or library to count same elements in that tuple 
    4.Now use combination to the values of dictionary to get the desired result 

    '''
    # To find possible substring
    # substring = [s[i: j] for i in range(len(s))
    #       for j in range(i + 1, len(s) + 1)] 
    
    substring_sorted = [sorted(s[i: j]) for i in range(len(s)) 
          for j in range(i + 1, len(s) + 1)] 

    substring_tup=map(tuple,substring_sorted)
    c=collections.Counter(substring_tup)
    combinations=0
    for key,values in c.items():
        if(c[key]>=2):
            combinations+=combination(c[key],2)     
    return combinations  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
