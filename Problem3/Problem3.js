var num = 600851475143;
var lfactor = 0;
var factors = [];

for (var i = 2; i * i < num; i++){
    if(num % i == 0){
        factors[0] = i;
        factors[1] = num / i;

        for(var k = 0; k < 2; k++){
            var isPrime = true;
            for( var j = 2; j * j < factors[k]; j++){
                if(factors[k]%j == 0){
                    isPrime = false;
                    break;
                }

            }
            if(isPrime && factors[k] > lfactor){
                lfactor = factors[k]
            }
        }
    }
}
console.log(lfactor)