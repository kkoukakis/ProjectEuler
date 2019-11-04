
var below = 1000
var sum = 0
var x = 0
for ( x = 0; x<below; x++){
    if(x%3==0){
        sum += x;
    }
    else if(x%5==0){
        sum += x;
    }
}
console.log(sum);