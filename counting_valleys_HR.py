
#https://www.hackerrank.com/challenges/counting-valleys/problem

"""
Hiker who avidly tracks hikes gives list of up steps vs down steps. Program tracks number of times he enters a valley on a hike

INPUT: total number of steps, list of step direction (ex: [UDUDDUUDDD])
OUTPUT: total number of valleys entered
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    #error handling
    if n<=1:
        return(0)

    #variable tracking
    step_force = 0
    step_total = 0
    valley_cnt = 0
    i = 0
    prior_step = "level"
    
    for hike_step in s:
        i += 1
        if hike_step == "U":
            step_force = 1
        else:
            step_force = -1
        step_total += step_force
        if step_total == 0:
            prior_step = "level"
        elif (prior_step =="level" and step_total == -1):
            valley_cnt += 1
            #return(i,valley_cnt, prior_step)
        else:
            prior_step = None
    return(valley_cnt)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
