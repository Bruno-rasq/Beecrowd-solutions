const input_1984 = `0123456789`

//const fs = require('fs')
//const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines_1984 = input_1984.split('\n')

let data_1984 = String(lines_1984.shift())
  .trim()
  .split('')
  .reverse()
  .join('')

console.log(data_1984)