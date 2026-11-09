#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # specifically find the num of letter a's in first n letters repeating s
    
    # I mean first off if no a's in s, then always 0
    if 'a' not in s:
        return 0 
    
    # # then see how many s fits within that len n str to calc num a's? 
    # if n % len(s) == 0:
    #     # then it's just the same frequency of a's within s
    #     return s.count('a') 
    # # otherwise it's more involved with partial s? 
    # commented out the above b/c it's tripping up some tests, probably for longer inputs
    
    # how many full repetitions of s fit into n
    full_repeats = n // len(s) 
    # remaining characters after full repetitions, 0 in shortcut above
    remainder = n % len(s)
    # * num a's in the reminder * 
    remainder_count = s[:remainder].count('a')
    return (full_repeats * s.count('a')) + remainder_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
