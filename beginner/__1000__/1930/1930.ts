const input_1930 = `6 6 6 6`

// const fs = require('fs')
// const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines_1930 = input_1930.split(' ').map(Number)

const result_1930 = lines_1930.reduce((curr: number, acc: number) => {
  return acc + curr
}, 0)

console.log(result_1930 - 3)