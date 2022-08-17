# goal to find the second largest value in an array 

if __name__ == '__main__':
    n = int(input())                  # number of array elements
    arr = map(int, input().split())
    
    max = -101
    # iterate through array to find the max
    for i in range(0,len(arr)):
        if arr[i] > max:
            max = arr[i]
    
    #print(max)
            
    # now create a new array, adding all non-max values from first array to new array 
    arr2 = [] 
    for i in range(0,len(arr)):
        if arr[i] < max:
            arr2.append(arr[i])
            
    #print(arr2)
    
    # now greatest value in arr2 will be the runner up
    max2 = -101
    for i in range(0,len(arr2)):
        if arr2[i] > max2:
            max2 = arr2[i]
            
    print(max2)                         # should be runner up value 
            