// #Copyright 2019-2020 kkoukakis
// #Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// #The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// #THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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