let a = 3;
let b = 2;

let result = 1 + (a / b)
while(b <= 39){
    a += 2
    b *= 2
    result += (a / b)
}

console.log(Math.round(result).toFixed(2))