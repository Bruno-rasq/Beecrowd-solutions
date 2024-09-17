const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const [a, b] = input.split(" ").map(Number)

const result = (
    ((1.0 + a / 100) * (1.0 + b / 100)) - 1.0
) * 100
console.log(result.toFixed(6))