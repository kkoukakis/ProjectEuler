import lib
import math
n=10000

for a in range(1,n):
    for b in range(a+1,n):
        c = lib.is_special(a, b )
        if(c is not 0):
            if lib.sum_is_equal_to(a, b , c , 1000):
                print(a*b*c)
                a = False
                break
        if a == False : break
    if a == False : break