#Project 4 Library

def is_palindrome(number):
    length = len(str(number))
    if(length == 1): return true
    array = [int((number % pow(10,x)) / pow(10,x-1)) for x in range(length,0,-1)]
    count = 0
    for x in range(0,int(length / 2)):
        if(array[x] != array[length-x-1]): 
            count+=1
    if(count!=0):
        return False
    else:
        return True