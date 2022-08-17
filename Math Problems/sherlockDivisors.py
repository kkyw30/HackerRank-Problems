#!/bin/python3

import math
import os
import random
import re
import sys

def divisors(n):
    if n % 2 == 1:
        return 0
    else:
        n /= 2 
        ans = 1 
        p = 2
        while p <= n:
            if p * p > n: 
                p = n
            e = 0
            while n % p == 0:
                e += 1 
                n /= p
            ans *= e + 1
            p += 1
    return ans

# alternate solution 
def divisors2(n):
    factors = [] 
    if n % 2 == 1:
        return 0
    else:
        for i in range(1, n+1):
            if n % i == 0 and i % 2 == 0:
                factors.append(i)

    return len(factors) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = divisors(n)

        fptr.write(str(result) + '\n')

    fptr.close()
