const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const [a, b] = input.split('\n').map(Number)

const soma = a + b

console.log(`X = ${soma}`)