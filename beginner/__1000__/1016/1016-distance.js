const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

let km = Number(lines[0]);
let time = km * 2;

console.log(`${time} minutos`);