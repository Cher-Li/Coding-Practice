#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    # special if either of these two: 
    # all char same, or all char except the middle same
    # this vaguely feels like a 2 ptr prob to get to the middle
    # and the slow ptr can focus on matching adjacent characters? 
    # I mean it's not returning whether it's a special string it's how many substrings fit the criteria <- and single characters are always valid
    
    # 1. consecutive identical char of len k has k(k+1)/2 substrings 
    # 2. all char except for middle identical -> [len k of consecutive X] + [1 char != X] + [another len k of consecutive X] 
    # latter is my idea of start from center and expand out, for ex aabaa -> bab and ababa, so min(len of left run, len of right run)
    if n == 0:
        return 0

    # * grouping consecutive characters: [(char, count), ...]
    groups = []
    count = 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
        else:
            groups.append((s[i - 1], count))
            count = 1
    groups.append((s[-1], count))

    total = 0

    # 1. substrings of single repeated char
    for _, c in groups:
        total += c * (c + 1) // 2

    # 2. middle char between matching char
    for i in range(1, len(groups) - 1):
        mid_char, mid_count = groups[i]
        left_char, left_count = groups[i - 1]
        right_char, right_count = groups[i + 1]

        # conditions of, center unique, left and right match and isn't the same as center
        if mid_count == 1 and left_char == right_char and left_char != mid_char:
            total += min(left_count, right_count)

    return total
    
    # brute force is just, count up all "1" len character substrings that fit, then all the "2" len if adj, and so on, but probably takes too long? 
    # could I loop through each char and see how many substrings it could be the middle of
    # num_substrings = 0
    # for i in range(len(s)):
    #     # 1. count s[i] itself
    #     # 2. want to check s[i] against s[i - 1] and s[i + 1] and keep incrementing that until i + or - j reaches 0 or len(s)? 
    #     # but this doesn't quite take care of something like "aa" where just 2 characters are the same, and this is still O(N^2) 
    # return num_substrings
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
