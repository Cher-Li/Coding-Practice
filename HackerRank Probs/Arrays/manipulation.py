#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    # naive approach: iter thr every index [a, b] for each of the m queries and adding k
    # * use difference arr -> record the start of the increment at index a (+k) and the end of the increment right after b (b + 1, -k)
    # single prefix sum pass computes the final array values and tracks the maximum value in linear time
    
    # difference array of size n + 2 to safely handle 1-indexing and b + 1 bounds
    arr = [0] * (n + 2)
    
    # * difference array updates per query
    for a, b, k in queries:
        arr[a] += k # from this point, add k
        if b + 1 <= n:
            arr[b + 1] -= k
            
    max_val = 0
    current_val = 0
    
    # prefix sums and find max <- use difference arr to reconstruct what would be the final arr for each index
    for i in range(1, n + 1):
        current_val += arr[i]
        if current_val > max_val:
            max_val = current_val
            
    return max_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
