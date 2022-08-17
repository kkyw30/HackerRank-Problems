import math
import os
import random
import re
import sys

# these mathematical calculations much easier in Python

def summingSeries(n):
    # series really just sums to n^2
    return n*n % 1000000007

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        print('n is', n)
        result = summingSeries(n)
        print(result) 
