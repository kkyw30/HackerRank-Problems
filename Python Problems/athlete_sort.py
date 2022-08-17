import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])              # number of athletes
    m = int(nm[1])              # number of attributes
    arr = []                    # list of lists 

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    arr.sort(key=lambda y: y[k])  # use lambda function (anonymous function) to sort the list of lists by the kth element in each list (y in lambda expression represents arbitrary list element)
    
    for l in arr: 
        string = ''
        for emnt in l:
            string += str(emnt)   # can only concatenate string to string in Python 
            string += ' '
        print(string) 
    
    
