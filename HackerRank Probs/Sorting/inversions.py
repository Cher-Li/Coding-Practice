#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countInversions(arr):
    # Write your code here
    # only swap adjacent elmts if wrong order, count num inversions
    # reminds me of min swaps prob, that one uses a cycle b/c it doesn't have to be adjacent elmts tho
    # brute force is just, bubble sort, but O(N^2)
    
    def merge_sort(sub): # * helper func
        n = len(sub)
        if n <= 1:
            return sub, 0

        mid = n // 2 # divide in half each time so O(n log n)
        left, left_inv = merge_sort(sub[:mid])
        right, right_inv = merge_sort(sub[mid:])
        # then just sum up left and right inversions

        merged = []
        inversions = left_inv + right_inv
        i = j = 0
        len_l = len(left)

        # * after splitting, need to merge back together interleavingly
        while i < len_l and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                # All remaining elements in left[i:] are greater than right[j]
                inversions += len_l - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inversions

    # call merge sort on the whole arr, can discard final merged
    _, total_inversions = merge_sort(arr)
    return total_inversions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
