"""
Problem Title : Ransom Note
Problem Statement: https://www.hackerrank.com/challenges/ctci-ransom-note/problem
Coding language : python 3

"""


#!/bin/python3

import math
import os
import random
import re
import sys
  
#from collections import Counter
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    #Thoughts :
    ''' Using dictionaries makes the solution easier 
    1.Convert both string inputs into maps or dictionary(note_map&magazine_map) with key as word and value as no of words count in that list
    2.Check if note map is subset of magazine map or if values present in magazine_map for words in notes is greater than that in note_map and count that occurance(see code below) and return desired result
    '''
    note_map=dict()
    for x in note:
        note_map[x]=note_map.get(x,0)+1  #note .get()func - if key's value found it returns that else set that key's value to 0

    magazine_map=dict()
    for x in magazine:
        magazine_map[x]=magazine_map.get(x,0)+1
    
    no_of_corrects=0

    for word in note:
        if magazine_map.get(word):  #using direct key here may throw key error if not found
            if(magazine_map[word]>=note_map[word]):
                no_of_corrects+=1

    
         
    
    if(no_of_corrects==len(note)):
        print("Yes")
    else:
        print("No")
            
     


    # OR Using collection.Counter library
    # if(Counter(note)-Counter(magazine)=={}):
    #     print("Yes")
    # else:
    #     print("No")

    return 


    
         





if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
