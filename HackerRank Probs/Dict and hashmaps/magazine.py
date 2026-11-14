#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

from collections import Counter # *

def checkMagazine(magazine, note):
    # Write your code here
    # so need to check frequency of words in magazine >= note
    # could brute force by building the full dictionary of word / count, case sensitive
    
    mag_counts = Counter(magazine)
    note_counts = Counter(note)
    
    for word, count in note_counts.items():
        if mag_counts[word] < count:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
