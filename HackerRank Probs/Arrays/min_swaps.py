#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    # not sure if overthinking this but want to swap with another num that's in the wrong position? like how would we know it's the min num of swaps
    # like, difference between its current index and its value - 1 aka where it should be, want to try to match a swap going left with a swap going right
    
    # * 
    n = len(arr)
    visited = [False] * n
    swaps = 0
    
    for i in range(n):
        # elmt already visited or already in its correct position
        if visited[i] or arr[i] == i + 1:
            continue
            
        # * cycle traversal - eventually chain loops back to where it started? 
        cycle_size = 0
        curr = i
        while not visited[curr]: # go through the cycle
            visited[curr] = True # mark where visited
            # move to index where cur elmt belongs (value - 1)
            curr = arr[curr] - 1
            cycle_size += 1

        # add to tot swaps
        if cycle_size > 1:
            swaps += (cycle_size - 1) 
            # * if a cycle len k, takes k - 1 swaps to sort all elements within that cycle
            
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
