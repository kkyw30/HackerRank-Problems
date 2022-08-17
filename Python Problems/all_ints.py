# goal to print out all digits, from 1 to n, as a single string (e.g. 3 -> '123')

if __name__ == '__main__':
    n = int(input())
    to_print = ''
    for i in range(1,n+1):
        to_print += str(i)
    print(to_print)