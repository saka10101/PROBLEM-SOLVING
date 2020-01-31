#!/bin/python3
"""
Problem Title :Flipping bits
Problem Statement: https://www.hackerrank.com/challenges/flipping-bits/problem
Coding language : python 3

"""
import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    #Simple mathematical approach
    '''
    Here we  XOR the value with 2^32 -1 (all 1 ie :1111 1111 1111 1111 1111 1111 ).
    we can also negate the value and add 2^32 aternatively
    In python logical bitwise operations in decimal base results the decimal(internally calculated)

    Interesting note related to use of xor in python:

    >>> # this example swaps integers without a temporary variable using XOR
    >>> a = 2
    >>> b = 8
    >>> a ^= b
    >>> b ^= a
    >>> a ^= b
    >>> a
    8
    >>> b
    2


    '''
    #return ~n + 2 ** 32
    return n ^  2 ** 32-1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
