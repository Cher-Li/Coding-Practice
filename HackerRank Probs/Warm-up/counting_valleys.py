#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # D is basically -1 and U is +1, returning num valleys (number of times go downwards and then up again?) <- or specifically like, breaching the 0 mark
    level = 0
    valleys = 0
    for i in range(steps):
        if path[i] == 'U':
            level += 1
        else:
            if level == 0: # * put here instead of checking if == -1
                valleys += 1 
            level -= 1
    
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
