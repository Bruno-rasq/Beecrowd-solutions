const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf8');
const [b, g] = input.split('\n').map(Number)

const result = parseInt((g /2) - b)

console.log(result <= 0 ? "Amelia tem todas bolinhas!" : `Faltam ${result} bolinha(s)!`)