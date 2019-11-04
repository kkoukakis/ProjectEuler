
var below_number = 4000000

var even_sum = 1
var a = 0
var b = 1
var skip = false

if (below_number == 0){
    console.log(a)
    skip = true
}
if(skip == false){
    while (b <= below_number){
        c = a + b
        a = b
        b = c 
        if((b % 2 == 1) &&( b <= below_number))
        {
            even_sum = even_sum + b
            //console.log(b)
        }
    }
    console.log(even_sum)
}