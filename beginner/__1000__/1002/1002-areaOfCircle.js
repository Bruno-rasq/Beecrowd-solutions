const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

let R = parseFloat(lines[0]);
let pi = 3.14159;

let Area = pi * (R**2);
console.log(`A=${Area.toFixed(4)}`);