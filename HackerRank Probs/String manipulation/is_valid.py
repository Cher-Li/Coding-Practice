#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

from collections import Counter
def isValid(s):
    # Write your code here
    
    char_counts = Counter(s)
    freq_counts = Counter(char_counts.values())

    # 1. already all same freq
    if len(freq_counts) == 1:
        return "YES" 

    # 2. exactly 2 distinct freq
    if len(freq_counts) == 2: 
        (f1, c1), (f2, c2) = freq_counts.items() # *

        # 1 char appears once, removing it drops it
        if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
            return "YES"

        # freq differ by 1 and the higher freq need to occur only once so after removing, they're all matching
        if abs(f1 - f2) == 1:
            higher_freq = max(f1, f2)
            higher_count = c1 if f1 == higher_freq else c2
            if higher_count == 1:
                return "YES"

    # otherwise > 2 frequencies or no single removal matches all
    return "NO"
    
    # # I mean, maybe just get frequency counts, and check that the "count" is only separated by 1? B/c can remove 1 occurrence? 
    # s_count = Counter(s)
    # all_counts = set(s_count.values())
    # if len(all_counts) > 2:
    #     return "NO"
    # # else they need to be only one apart? I guess there's still cases where that doesn't work, like if frequencies are 2 2 3 3, still can't get all of them to match
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
