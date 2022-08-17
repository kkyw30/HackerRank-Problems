from itertools import product 

if __name__ == '__main__':
    # get the K and M values
    K, M = map(int, input().split()) 
    
    # trying to maximize the REMAINDER, not the values squared
    next_lists = []
    for _ in range(K):
        next_list = list(map(int, input().split()))   # map to a list of ints
        del next_list[0]                              # delete element representing # of values (may somehow contribute to a higher remainder)
        next_lists.append(next_list) 
        
    all_combos = list(product(*next_lists))   # returns list of all combos resulting from choosing from each list
    
    maxes = [] 
    for l in all_combos:
        square_sum = sum([x**2 for x in l])
        maxes.append(square_sum % M)
        
    print(max(maxes))
        
         
            
    