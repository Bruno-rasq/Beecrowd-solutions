const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

let A = parseFloat(lines[0]);
let B = parseFloat(lines[1]);

let MEDIA = (((A * 3.5) + (B * 7.5)) / (3.5 + 7.5));
console.log(`MEDIA = ${MEDIA.toFixed(5)}`);