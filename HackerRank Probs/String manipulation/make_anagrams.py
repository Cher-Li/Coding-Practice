#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

from collections import Counter

def makeAnagram(a, b):
    # Write your code here
    # minimum number of character deletions 
    # required to make a and b anagrams
    # always want to remove from the longer length? 
    # deals w/ freq so I'm guessing need counters: 
    count_a = Counter(a)
    count_b = Counter(b)
    
    deletions = 0
    all_chars = set(count_a.keys()) | set(count_b.keys()) 
    
    for ch in all_chars:
        deletions += abs(count_a[ch] - count_b[ch]) # * need to have same frequencies for each character
        # in one but not the other -> remove 
        # otherwise just match frequency
        
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
