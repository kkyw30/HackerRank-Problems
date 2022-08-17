# goal to print a palindromic triangle of a given size

for i in range(1,int(input())+1):
    print(((10**i - 1)//9)**2)