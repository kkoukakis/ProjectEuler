#Project 3 Library
import math

def is_prime(num):
    if num <= 1: return False
    if num == 2: return True
    if num % 2 == 0: return False
    if num < 2: return False
    root = int(math.sqrt(num)) + 1
    # print('ROOT:' ,root)
    for i in range(3,root,2):
        if ( num % i ) == 0: return False
    return True
