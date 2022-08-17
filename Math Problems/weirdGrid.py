import math
import os
import random
import re
import sys

# find number at row r and column c 
def strangeGrid(r, c):
    rowStart = (r - 1) // 2 * 10    # do integer division 
    if (r - 1) % 2 == 1:
        rowStart += 1
    return (rowStart + (c - 1) * 2)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    r = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    result = strangeGrid(r, c)
    print(str(result) + '\n')
