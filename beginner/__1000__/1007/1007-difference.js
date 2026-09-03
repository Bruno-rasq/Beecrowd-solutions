const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

let A = Number(lines[0]);
let B = Number(lines[1]);
let C = Number(lines[2]);
let D = Number(lines[3]);

let DIFFERENCE = ((A * B) - (C * D));
console.log(`DIFERENCA = ${DIFFERENCE}`);