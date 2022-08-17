# goal to find angle mbc in degrees

import math

if __name__ == '__main__':
    ab = int(input())
    bc = int(input())
    
    ac = math.sqrt(ab*ab + bc*bc)    # find hypotenuse length
    mc = ac / 2.0
 
    # use law of cosines to find length MB 
    x1 = math.degrees(math.atan(ab/bc))
    mb = math.sqrt(mc*mc + bc*bc - 2*mc*bc*math.cos(x1))
    
    # mbc should be the same as ACB
    mbc = x1
    mbc = int(round(mbc))
    print(str(mbc)+'\u00B0')