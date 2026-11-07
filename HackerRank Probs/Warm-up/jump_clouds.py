#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # jump on cloud with number equal to current cloud plus 1 or 2
    # num being index? so c[i + 1] or c[i + 2], avoiding "1"s
    # maybe a dp problem where you find the min result for each? 
    
    jumps = 0
    i = 0
    n = len(c)
    
    while i < n - 1: # since 0-based index
        if i + 2 < n and c[i + 2] == 0: # greedy approach, just keep jumping 2 and only 1 if that's not possible <- emphasis on it's always winnable
            i += 2
        else:
            i += 1
        jumps += 1
    
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
