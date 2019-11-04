
big = 1 * 2 * 3 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20
done=-1
for i in range(0,big, 10):
    count = 0
    for x in range(11,20):
        #print("try:",i)
        if i % x == 0:
            count += 1
           # print(count)
    if count == 9:
        done+=1
        if done is 1:
            print("correct:",i)
            break
    count = 0