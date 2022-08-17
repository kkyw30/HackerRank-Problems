# goal to print out all the results of groupby(string)

from itertools import groupby 
if __name__ == '__main__':
    s = input() 
    # print out all (*) the tuples (len,k) in groupby(s)
    print(*[(len(list(c)), int(k)) for k, c in groupby(s)])