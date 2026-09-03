const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')
const pi = 3.14159;

let R = parseFloat(lines[0]);

let Area = pi * Math.pow(R, 2);

console.log(`A=${Area.toFixed(4)}`);