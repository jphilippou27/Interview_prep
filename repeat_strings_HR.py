#!/bin/python3

#question prompt: https://www.hackerrank.com/challenges/repeated-string/problem

"""
find number of times the letter 'a' appears in a string

INPUT: string of lower case letters, number of times the string repeats
OUTPUT: Number of times a appears
"""

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    #edge case of a single character
    if len(s) == 1 and s == 'a':
        result = n
        return (result)
    #handle null string
    if len(s) ==0:
        result = 0
        return (result)
    #count of 'a' in non-repeat string
    a_result = 0 
    for letter in s:
        if letter == 'a':
            a_result += 1 
    #handling repeat of string  
    repeat_cnt = 0
    repeat_cnt = int(n/len(s))
    extra = n %len(s)
    #fixing strings of odd lengths
    extra_cnt = 0
    extra_letters = s[:extra]
    for e in extra_letters:
        if e == 'a':
            extra_cnt += 1
    #tallying counts
    result = a_result * repeat_cnt + extra_cnt
    
    return(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
