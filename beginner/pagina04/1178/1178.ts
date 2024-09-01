const input_1178 = `200.0000`

//const fs = require('fs')
//const input = fs.readFileSync('/dev/stdin', 'utf-8')
let lines_1178 = Number(input_1178)

let idx = 0
while (idx < 9){
  console.log(`N[${idx}] = ${lines_1178.toFixed(4)}`)
  lines_1178 /= 2
  idx++
}