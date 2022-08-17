# goal to calculate the hash of a tuple

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input.split())

    t = () 
    for i in integer_list:
        t = t + (i,)         # syntax for appending elements to tuples

    print(hash(t))