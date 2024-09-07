const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

let A = parseFloat(lines[0]);
let B = parseFloat(lines[1]);
let C = parseFloat(lines[2]);

let MEDIA = (((A * 2) + (B * 3) + (C * 5)) / (2 + 3 + 5));
console.log(`MEDIA = ${MEDIA.toFixed(1)}`);