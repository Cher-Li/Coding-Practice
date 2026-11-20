#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    # so we want the max of taking a toy but subtracting the price from k, or not taking the toy <- ok this is for 0/1 knapsack where each "toy" has a different value, here it's all +1 
    # not sure how sorting comes into play, sort by most vs least expensive? 
    # yea so greedy approach, get the most cheapest toys to max number of toys
    
    prices.sort()
    count = 0

    for price in prices:
        if price <= k:
            k -= price
            count += 1 # just keep adding num toys until k threshold
        else:
            break

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
