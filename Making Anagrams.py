"""
Problem Title :Strings: Making Anagrams
Problem Statement: https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
Coding language : python 3

"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.

def frequency_map(s): 
    f_map = {}
    for char in s:
        if char not in f_map:
            f_map[char] = 1
        else:
            f_map[char] +=1
 
    return f_map    
        
    
def makeAnagram(a, b):
    '''
    Approach:
    1.Convert the strings into map with each character's frequency count ,here frequency_map() does this
    2.Now compare these two maps and get result
     - Use a tracker to calculate no of characters to be deleted in particular string(here we have two of them), in the code deletes_count does this work
     - Check if same key lies in those both maps and update the difference accordingly
        - if yes find out not of char to be deleted in context of particular string fmap ,here for this we can utilize max(0,exp) way 
        - if not add delete all those char counts in the particular map 
        - keep tracking or summing the chars to be deleted using difference tracker in each case and return the final result (ie total chars to be deleted from both            strings)
    
    '''
    map_a=frequency_map(a)
    map_b=frequency_map(b)
    
    deletes_count= 0
    for key in map_a.keys():
        if key not in map_b.keys():
            deletes_count+= map_a[key]
        else:
            deletes_count+= max(0,map_a[key]-map_b[key]) # This is wrong =>abs(map_a[key]-map_b[key]) as we don't want this #

    #keep on adding chars to be deleted from another string ...

    for key in map_b.keys():
        if key not in map_a.keys():
            deletes_count += map_b[key]
        else:
            deletes_count+= max(0,map_b[key]-map_a[key]) 



    return deletes_count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
