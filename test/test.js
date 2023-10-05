// let input = require('fs').readFileSync("./test/stdin", 'utf8');
// let lines = input.split('\n');

console.log(" 2693 - Van ");

const input = `5
Samuel O 1
Fabricio L 1
Emanuel S 3
Kaio S 20
Hugo N 90`;

let lines = input.split('\n');
let int = Number(lines.shift());

for(let i = 0; i < int; i++){

    let data = lines[i].split(' ')
    console.log(data)

}