def has_over_factors(array,num_of_factors,length):
    for j in range(1,length):
        number = array[j-1]
        factors = 0
        for i in range(1, number):
            if number % i == 0:
               factors+=1
            if factors > 500:
                return number
    return 0   

done = False

array = []
i = 1000
while i in range(1000,10000):
    array.append(int(i*(i+1)/2))
    i+=1
print(has_over_factors(array,500,len(array)))
