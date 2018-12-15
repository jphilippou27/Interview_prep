#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    #error handling
    if len(ar)< 1:
        return 0

    #tracking number
    sock_pair_total = 0
    pair_per_key = 0

    #converting list into a dictionary
    sock_dict = dict()
    for i in ar:
        sock_dict[i] = sock_dict.get(i,0) + 1
    #return (sock_dict)
    #finding pairs of socks via keys
    for sock_ids, sock_counts in sock_dict.items():
        pair_per_key = int(sock_counts/2)
        sock_pair_total += pair_per_key
    return(int(sock_pair_total))


#put in dictionary, iterate over dict keys, count even number of items for each key

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
