#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

from collections import Counter

def sherlockAndAnagrams(s):
    # Write your code here
    # anagram true or false - same frequency of counts, but we're trying to find the num of substrings (so never the full string) that both exist in the original str <- need repeated characters at least? 
    signatures = Counter() 
    n = len(s)

    # generate all possible substrings, implicitly handles the "full string isn't part of the answer" since only 1 of it
    for i in range(n): 
        for j in range(i + 1, n + 1): 
            # sorting substr = unique signature for anagrams
            sub = "".join(sorted(s[i:j]))
            signatures[sub] += 1

    # * for any signature appearing k times, k * (k - 1) // 2 unordered pairs
    total_pairs = 0
    for count in signatures.values():
        total_pairs += count * (count - 1) // 2 # k choose 2

    return total_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
