#!/bin/python3

import math
import os
import random
import re
import sys

# from collections import Counter
from collections import defaultdict
# Complete the freqQuery function below.
def freqQuery(queries):
    # for each query, queries[i][0] is one of the 3 operations, while queries[i][1] is the actual data
    # I guess naive method is just loop through all queries and take care of each case on its own
    results = []
    
    # * 
    element_count = defaultdict(int) # freq for each number
    freq_count = defaultdict(int) # how many numbers share a specific freq count
    # just keep running count of freq along the way instead
    
    for operation, data in queries:
        if operation == 1:
            old_freq = element_count[data]
            if old_freq > 0:
                freq_count[old_freq] -= 1 # decrement this frequency "bucket" 
                if freq_count[old_freq] == 0:
                    del freq_count[old_freq]
            
            new_freq = old_freq + 1
            element_count[data] = new_freq
            freq_count[new_freq] += 1 # add to new freq bucket
            
        elif operation == 2:
            old_freq = element_count[data]
            if old_freq > 0:
                freq_count[old_freq] -= 1 # still decrement freq bucket
                if freq_count[old_freq] == 0:
                    del freq_count[old_freq]
                
                new_freq = old_freq - 1
                if new_freq > 0: # if there's still occurences, reassign freq bucket
                    element_count[data] = new_freq
                    freq_count[new_freq] += 1
                else:
                    del element_count[data]
                    
        elif operation == 3:
            if freq_count[data] > 0: # if the bucket for that z freq has a count
                results.append(1)
            else:
                results.append(0)
                
    return results
    
    # arr = []
    # for query in queries:
    #     operation, data = query
    #     if operation == 1:
    #         # insert
    #         arr.append(data) # O(1) 
    #     elif operation == 2:
    #         # delete is present, continue if not
    #         if data in arr:
    #             arr.remove(data) # O(N) so not the best
    #     else: # since always 1-3
    #         # check if freq = z so possibly a counter here
    #         # if freq is same as data, append to results arr? 
    #         freq = Counter(arr) # also O(N) 
            
    #         if data in freq.values():
    #             results.append(1)
    #         else:
    #             results.append(0)
    # return results    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
