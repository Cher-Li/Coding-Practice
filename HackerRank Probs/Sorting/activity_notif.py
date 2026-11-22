#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    # number of notif =  If the amount spent by a client on a particular day is greater than or equal to 2x median spending for trailing num of days aka range to index - d
    # maybe a sliding window style, for each new num, add the newest and remove the first item, but maybe maintain some other data structure for easy sorting to calc median
    
    max_val = 200 # expenditure[i] constrained
    freq = [0] * (max_val + 1) # this data structure, freq arr, even if arr is long each num is small

    # init freq counts for the first window of size d
    for i in range(d):
        freq[expenditure[i]] += 1

    # * median from cumulative counts
    def get_kth_value(k):
        count = 0
        for val in range(max_val + 1):
            count += freq[val]
            if count >= k:
                return val
        return max_val
    # smallest value st sum of freq[0..v] is at least k

    notifications = 0
    is_odd = (d % 2 == 1)
    mid_odd = d // 2 + 1
    
    mid_even_left = d // 2
    mid_even_right = d // 2 + 1

    for i in range(d, len(expenditure)):
        current_spend = expenditure[i]

        if is_odd:
            # mid = d // 2 + 1
            # expenditure[i] >= 2 * get_kth(mid)
            median_val = get_kth_value(mid_odd)
            if current_spend >= 2 * median_val:
                notifications += 1
        else:
            # median is avg of d // 2 and d // 2 + 1
            left_val = get_kth_value(mid_even_left)
            right_val = get_kth_value(mid_even_right)
            if current_spend >= left_val + right_val:
                notifications += 1

        # slide window, remove oldest day, add newest
        freq[expenditure[i - d]] -= 1
        freq[current_spend] += 1

    return notifications
    # time complex O(n * M) and M is 201, space complex O(M)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
