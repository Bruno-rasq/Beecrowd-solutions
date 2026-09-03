const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

let time = Number(lines[0]);
let kmh = Number(lines[1]);

let response = ((time * kmh) / 12);

console.log(response.toFixed(3));