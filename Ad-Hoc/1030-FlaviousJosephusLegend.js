console.log(" 1030 - Flavious Josephus Legend ");

const input = `2
5 2
6 3`;

let lines = input.split('\n');
let int = Number(lines.shift());

for(let i = 0; i < int; i++){

    let [ a, b ] = lines.shift().split(' ').map(el => Number(el))
    let testando = test(a, b)

    console.log(`Case ${i+1}: ${testando + 1}`)
}

function test(n, k){

    if(n == 1) return 0;
    return (test(n - 1, k) + k) % n;
}