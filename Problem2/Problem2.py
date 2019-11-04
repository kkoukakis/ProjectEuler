below_number = 4000000

even_sum = 1
a = 0
b = 1
skip = False

if below_number == 0:
    print(a)
    skip = True

if skip == False:
    while (b <= below_number):
        c = a + b
        a = b
        b = c 
        if(b % 2 == 1 and b <= below_number):
            even_sum = even_sum + b
           #print(b)
    print(even_sum)

