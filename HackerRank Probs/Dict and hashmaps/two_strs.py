#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

from collections import Counter

def twoStrings(s1, s2):
    # Write your code here
    # I mean base case is like, if they share at least one letter, since this isn't looking for the longest substr
    # s1_counts = Counter(s1)
    # s2_counts = Counter(s2) 
    # then just, check whether they share at least one letter? 
    # do you even need a counter if you're just checking whether they share a letter instead of the count
    for char in s1:
        if char in s2:
            return "YES"
    
    return "NO" 
    # O(N x M) where N and M are lengths? 
    
    # ok that works, but could also optimize: 
    # return "YES" if set(s1) & set(s2) else "NO" 
    # O(N + M), set automatically removes duplicates, just see if they share
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
