const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf8')
const lines = input.split('\n')

let x = Number(lines[0])
let y = parseFloat(lines[1])

let average = x / y

console.log(`${average.toFixed(3)} km/l`)