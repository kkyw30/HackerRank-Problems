if __name__ == '__main__':
    T = int(input()) 
    
    for i in range(0,T):
        flag = False                  # indicator for what we should print at end
        
        # obtain the sets A and B 
        length_A = int(input()) 
        A = input().split(' ') 
        length_B = int(input()) 
        B = input().split(' ') 
        
        # check that B is equal to or longer than A 
        if length_A > length_B:
            flag = False  
        
        counter = 0
        for emnt in A:
            if emnt in B:
                counter += 1 
                continue
            else:
                flag = False
        
        # make sure all the elements of A are in B
        if counter == length_A:
            flag = True 
            
        if flag:
            print('True')
        else:
            print('False') 
            
        
        
        