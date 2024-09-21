const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

let notaA = parseFloat(lines[0])
let notaB = parseFloat(lines[1])
let notaC = parseFloat(lines[2])

let MEDIA = (((notaA * 2) + (notaB * 3) + (notaC * 5)) / (2 + 3 + 5))

console.log(`MEDIA = ${MEDIA.toFixed(1)}`)