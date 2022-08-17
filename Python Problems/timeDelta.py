#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return str(int(abs((t1-t2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


# if we were to do this manually, without built-in functions from datetime library 
if __name__ == '__main__':
    N = int(input())
    
    all_stats = [] 
    for i in range(0,2*N):
        t1 = input() 
        words = t1.split(' ') 
        all_stats.append(words)
        
    for i in range(0, len(all_stats)):
        if i % 2 == 0:
            year1 = all_stats[i][3]
            year2 = all_stats[i+1][3]
            
            month1 = all_stats[i][2]
            month2 = all_stats[i+1][2] 
            
            day1 = all_stats[i][1]
            day2 = all_stats[i+1][1]
            
            hour1 = all_stats[i][5]
            hour2 = all_stats[i+1][5]
            
            days = abs(int(day1) - int(day2)) 
            hours = abs(int(hour1) - int(hour2))
            hours = (hours % 100) / 60 + hours // 100 
            
            time_seconds = days * 24 * 3600 + hours * 3600
            print(time_seconds) 
            
        # want to look at two stats at a time
        else: 
            continue 
        
        
        
    

