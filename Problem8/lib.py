def num2array(number):
    length = len(str(number))
    array = [int((number % pow(10,x)) / pow(10,x-1)) for x in range(length,0,-1)]
    return array