below = 1000
sum = 0
for x in range(0,below):
    if x % 3 == 0:
        sum = sum + x
    elif x % 5 == 0:
        sum = sum + x
print(sum)