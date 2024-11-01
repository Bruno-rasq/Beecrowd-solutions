const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const [hobbits, km] = input.split(' ').map(Number)

hobbits += 2;
let result = km / hobbits;

console.log(result.toFixed(2))