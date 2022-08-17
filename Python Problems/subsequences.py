# goal to find all substrings of a given string, in lexicographic order, of a certain size

from itertools import combinations_with_replacement

if __name__ == '__main__':
    raw = input() 
    str = raw.split()[0]
    n = int(raw.split()[1])
    str = ''.join(sorted(str))    # sort the string alphabetically
    
    l = list(combinations_with_replacement(str, n))
    for emnt in l:
        result = ''
        for i in range(0,n):
            result += emnt[i] 
        print(result)