const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const km = Number(input)

let time = km * 2

console.log(`${time} minutos`)