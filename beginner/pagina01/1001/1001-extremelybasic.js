const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

let A = Number(lines[0]);
let B = Number(lines[1]);
let X = A + B;

console.log(`X = ${X}`);