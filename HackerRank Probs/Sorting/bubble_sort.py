#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    n = len(a)
    swaps = 0
    
    for i in range(n): 
        for j in range(n - 1): 
            # Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]): 
                placeholder = a[j + 1]
                a[j + 1] = a[j]
                a[j] = placeholder
                # or just directly a[j], a[j + 1] = a[j + 1], a[j]
                
                swaps += 1
    
    print("Array is sorted in " + str(swaps) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1])) 
    
    # print(f"Array is sorted in {swaps} swaps.")
    # print(f"First Element: {a[0]}")
    # print(f"Last Element: {a[-1]}")
    


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
