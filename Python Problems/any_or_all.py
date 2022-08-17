def isPalindrome(some_num):
    num_string = str(some_num)
    for i in range(0,len(num_string)):
        if num_string[i] == num_string[len(num_string) - i - 1]:
            continue
        else:
            return False 
    return True 

def isPositive(some_num):
    return some_num > 0

if __name__ == '__main__':
    N = int(input()) 
    
    nums = [int(x) for x in input().split(' ')]   # turn into list of ints using list comprehension
    #[print(isPalindrome(x)) for x in nums]
    if all([isPositive(x) for x in nums]):        # use all() and list comprehension
        print(any([isPalindrome(x) for x in nums]))
    else:
        print(False) 