import math
def is_special(a,b):
    c = a**2 + b **2
    c = math.sqrt(c)
    if c == int (c):
        return int(c)
    else :
        return 0

def sum_is_equal_to(a,b,c,target):
    if a+b+c == target:
        return True
    else:
        return False
