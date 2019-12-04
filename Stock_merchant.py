"""
Problem Title :Sock Merchant
Problem Statement: https://www.hackerrank.com/challenges/sock-merchant/problem
Coding language : python 3

"""
#
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

     """-Thougths
       We can realize the large pile of sock into key value pair structure where keys represents the type of sock (ie integer number representation of sock) and value the count of the particular sock.
        finally we can determine if there are pairs of socks present and count it 

     """

    pairscount=0
    d = {x:ar.count(x) for x in ar}
    a, b = d.keys(), d.values()

    for key in d:
        pairscount+=int(d[key]/2)

    return pairscount







if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()