# goal to return all coords (x,y,z) where x + y + z != some input n 

if __name__ == '__main__':
    x = int(input()) + 1
    y = int(input()) + 1
    z = int(input()) + 1
    n = int(input()) + 1

    # using list comprehensions
    ans = [[i,j,k] for i in range(x) for j in range(y) for k in range(z) if ((i+j+k) != n)]
    print(ans) 

    # using multiple for loops 
    coords = [] 
    for i in range(0,x):
        for j in range(0,y):
            for k in range(0,z):
                if (i + j + k != n):
                    coord = [] 
                    coord.append(i)
                    coord.append(j)
                    coord.append(k)
                    coords.append(coord)
    print(coords) 