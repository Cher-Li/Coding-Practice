#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    # I mean I think it's best to keep an anchor of the top left elmt
    # and so hourglass is sum of that, col + 1 and col + 2, then row + 1 as well as col + 1, and so on <- and if out of bounds just continue
    # then keep count = max(count, new_count)
    
    max_sum = -float('inf') # * start w/ -inf instead of 0 in case all neg
    
    # all top left corners
    for i in range(4):
        for j in range(4):
            current_sum = (
                arr[i][j]     + arr[i][j+1]   + arr[i][j+2] +
                                arr[i+1][j+1]               +
                arr[i+2][j]   + arr[i+2][j+1] + arr[i+2][j+2]
            )
            
            if current_sum > max_sum:
                max_sum = current_sum
                
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
