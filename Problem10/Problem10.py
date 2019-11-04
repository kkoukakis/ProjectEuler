import lib

sum = 2
below = 2000000
for i in range(3,below,2):
    if lib.is_prime(i):
        sum += i
print (sum)