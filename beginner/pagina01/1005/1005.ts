const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

let A = parseFloat(lines[0])
let B = parseFloat(lines[1])
let peso1 = 3.5
let peso2 = 7.5

let MEDIA = (((A * peso1) + (B * peso2)) / (peso1 + peso2))

console.log(`MEDIA = ${MEDIA.toFixed(5)}`)