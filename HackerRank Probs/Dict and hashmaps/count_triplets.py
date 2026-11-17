#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    # do we know if the array is ordered
    # r > 1 so it's always searching for an increasing triplet
    # I think brute force is just keep a counter at the "start" of each triplet and checking if it's a triplet
    # count = 0
    # for start in range(len(arr) - 1): 
    #     if arr[start] * r == arr[start + 1] and arr[start + 1] * r == arr[start + 2]:
    #         count += 1
    # return count
    # ofc that only works if searching for consecutive triplets, which this doesn't have to be
    # maybe directly having possible i, j, k, check first that i * r == j, then search for any that fits what k is supposed to be? 
    
    # * v2 is freq of elmts waiting to be the second in the triplet, v3 for the third
    v2 = Counter()
    v3 = Counter()
    count = 0
    
    for num in arr:
        # if cur number completes triplet, add its frequency to count
        if num in v3:
            count += v3[num]
            
        # if cur num can be second elmt, push expected third elmt into v3
        if num in v2:
            v3[num * r] += v2[num] # * 
            
        # cur num can always start a new triplet
        v2[num * r] += 1
        
    return count
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
