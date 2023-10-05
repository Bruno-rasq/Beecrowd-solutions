// let input = require('fs').readFileSync("./test/stdin", 'utf8');
// let lines = input.split('\n');

console.log(" 1548 - Carteen queue ");

const input = `3
3
100 80 90
4
100 120 30 50
4
100 90 30 25`;

let lines = input.split('\n');
let int = Number(lines.shift());

let response = []

for(let i = 0; i < int; i++){

    let integers = lines.shift()
    let arry = lines.shift().split(' ')

    let arrySorted = [...arry].sort((a, b) => b - a)
    
    let count = 0;

    for(let n = 0; n < integers; n++){

        if(arry[n] == arrySorted[n]){
            count++
        }

    }
    
    response.push(count)
}

console.log(response.join('\n'))