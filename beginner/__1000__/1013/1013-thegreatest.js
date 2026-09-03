const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'uft-8')
const lines = input.split('\n')

let [ a, b, c ] = lines[0].split(' ');
let arry = [];
arry.push(a, b, c);

let maior = Math.max(...arry);
console.log(`${maior} eh o maior`);