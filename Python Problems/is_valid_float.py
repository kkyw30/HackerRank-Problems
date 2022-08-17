# goal to determine whether a given string represents a valid float

# to read in input from stdin 
import sys 
    
# method to determine if string represents a float
def is_Float(n):
    # take care of possible exceptions
    try:
        num = float(n)
    except ValueError:
        #print('n is not a float')
        return False 
        
    # now determine whether first character is valid
    if n[0] != '+' and n[0] != '-' and n[0] != '.' and not n[0].isdigit():
        return False 
    
    # no more +/- symbols after first character
    dots = 0
    for i in range(1,len(n)):
        if n[i] == '+' or n[i] == '-':
            return False 
        if n[i] == '.':
            dots += 1
            
    # can only be one decimal point
    if dots != 1:
        return False
    
    num_list = n.partition('.')         # separate String at the decimal point
    decimals = num_list[2]
    decimals = decimals.replace('\n','')   # remove the new line character at end of string
    for i in range(0,len(decimals)):
        digit = decimals[i].isdigit()
        #return False 
        
    return True                         # true if passes all the other checks
    
infile = sys.stdin 
next(infile)                            # skip first line 
for line in infile: 
    bool = is_Float(line)
    print(bool)