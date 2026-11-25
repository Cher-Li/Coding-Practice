#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    # no matching adj characters <- I mean brute force would just be, loop through all char, double check each adjacent char is different
    # if create new string (probably not the right way), can get answer through their length difference
    deletions = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]: # just directly compare yea, if different, delete one
            deletions += 1

    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
