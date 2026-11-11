#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    # min num of bribes to get to order when any person can swap with its neighbor at most twice <- each num should be within two indices from its original? 
    
    bribes = 0
    for i, n in enumerate(q):
        # yea, if anyone moved more than 2 places
        if n - (i + 1) > 2:
            print("Too chaotic")
            return
        
        # * count how many people originally positioned behind n have moved ahead of it
        for x in range(max(n - 2, 0), i):
            # only look backward from the person's current index i down to max(n - 2, 0), 0 is just the bound, valid range
            if q[x] > n: # see how many larger original nums got ahead of the smaller ones (are now left of n) 
                bribes += 1
                
    print(bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
