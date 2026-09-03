const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const raio = parseFloat(input)

const circunferencia = 2 * (raio * 3.14)

console.log(circunferencia.toFixed(2))