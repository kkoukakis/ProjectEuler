
def has_over_factors(number,num_of_factors):
    a = number
    found = False
    x = 1
    factors = 0
    while a % x == 0:
        print(factors)
        factors += 1
        x += 1
        if factors > 500:
            found = True
            break
        if x > a: 
            return 0
    return a

done = False
i = 500000
while done is False:
    a = int(i*(i+1)/2)
    print("Number:",a)
    result = has_over_factors(a,500)
    print("Number_of_factors:",result)
    if result > 0:
        print(result)
        break
    i+=5

