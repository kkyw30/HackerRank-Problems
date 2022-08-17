import math
import os
import random
import re
import sys
import operator as op 
from functools import reduce

# helper method to find n C r 
def combinations(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

# total number of combinations is 2**n - 1
def lights(n):
    return (2**n-1)%10**5
        
# alternative solution (for smaller inputs) 
def lights2(n):
    sum = 0 
    # total sum will be sum of n C r for all r is less than n 
    for i in range(1, n+1):
        sum += combinations(n, i)
    return sum 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = lights(n)

        fptr.write(str(result) + '\n')

    fptr.close()
