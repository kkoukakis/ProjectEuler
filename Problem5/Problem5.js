
var big = 1 * 2 * 3 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20
var done=-1;
for(var i = 0; i< big; i+=10){
    var count = 0
    for(var x = 11; x<20; x++){
        // #print("try:",i)
        if (i % x == 0)
            count += 1
        //    # print(count)
        if (count == 9){
            done++
            if (done == 1){
                console.log("correct:" + i)
                break
            }
        }
    count = 0
    }
}