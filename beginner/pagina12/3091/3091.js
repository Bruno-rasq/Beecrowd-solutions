const fs = require("fs")
const input = fs.readFileSync("/dev/stdin", 'utf8')
const [a, b] = input.split('\n').map(Number)

console.log(a % b);