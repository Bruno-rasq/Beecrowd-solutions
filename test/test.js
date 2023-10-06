// let input = require('fs').readFileSync("./test/stdin", 'utf8');
// let lines = input.split('\n');

console.log("1023 - drought");

const input = `1 25
2 10 
3 10 
2 20 
6 11`;

let lines = input.split('\n');

let A = []
let B = []

for(let i = 0; lines.length; i++){

    let data = lines.shift().split(' ').map(el => Number(el))
    let [ a, b ] = data;

    A[i] = a
    B[i] = b

}

let test = B.filter((este, i) => {
    return B.indexOf(este) === i;
});

console.log(lines)
console.log(A)
console.log(B)
console.log(test)