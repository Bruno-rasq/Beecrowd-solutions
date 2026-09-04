const fs = require("fs")
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split(' ').map(Number)

console.log(lines.includes(9) ? 'F' : 'S')