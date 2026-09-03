const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

let A = Number(lines.shift())
let B = Number(lines.shift())
let C = Number(lines.shift())
let D = Number(lines.shift())

let DIFFERENCE = ((A * B) - (C * D))

console.log(`DIFERENCA = ${DIFFERENCE}`)