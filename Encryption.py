"""
Problem Title :Encryption
Problem Statement: https://www.hackerrank.com/challenges/encryption/problem
Coding language : python 3

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.

def encryption(s):

    #Thoughts:
    
    s_temp=s.replace(" ","") #first we create a temp string removing space but letters same as that input string
    L=len(s)    #calculate the length of string
    columns=int(math.ceil(L**(0.5))) #determine columns using ceiling function
    rows=int(columns)-1 #determine rows with the help of columns


    if rows*columns<L: # to ensure that rows*columns<=L
        rows=columns

    grid=[]   #Suppose an empty grid (in the form of list) first

    # Now filling out grid

    for x in range(rows):   #ie for each rows 
        grid.append(s_temp[:columns]) #append to grid the first columns letters of s_temp string 
        s_temp=s_temp[columns:] # update s_temp to hold remaining of s_temp that is not appended to grid(note the inclusive range)


    s_encrypted=''  #define an empty encrypted string

    #Now getting values from grid into encrypted string 

    for i in range (columns):
        for j in range(rows):
            if(i<len(grid[j])):
                s_encrypted+=grid[j][i]
        s_encrypted+=" "   #finally append spaces after each column traversal

    return s_encrypted


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

