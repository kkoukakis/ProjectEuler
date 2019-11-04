

import sys
from lib import is_palindrome
largest = 0
lx=0
ly=0
for x in range(100,999):
    for y in range(100,999):
        if(is_palindrome(int(x*y))):
            if(largest< (int(x*y)) ):
                largest = (int(x*y))
                lx=x
                ly=y
            
print(largest)