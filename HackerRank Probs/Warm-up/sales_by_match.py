#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # maybe do a count of all unique colors and just add to a running total if above 2 and even? <- or do it on the fly with a set, if seen, increment
    pairs = 0
    seen = set()
    
    for i in range(n):
        if ar[i] in seen:
            seen.remove(ar[i]) # this notation
            pairs += 1
        else:
            seen.add(ar[i])
    
    return pairs
    
    # or the below from my original idea of counting 
    # from collections import Counter
    # def sockMerchant(n, ar):
    #     return sum(count // 2 for count in Counter(ar).values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
