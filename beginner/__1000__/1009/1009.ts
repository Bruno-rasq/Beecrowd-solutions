const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

lines.shift() //nnumero do empregado não é relevante

let salary = parseFloat(lines.shift())
let sales = parseFloat(lines.shift())

let Bonus = ((sales * 15) / 100)
let salaryWithBonus = salary + Bonus

console.log(`TOTAL = R$ ${salaryWithBonus.toFixed(2)}`)