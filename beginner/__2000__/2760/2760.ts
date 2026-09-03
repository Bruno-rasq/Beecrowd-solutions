const input_2760 = `Roberto
carlos
aldo`

//const fs = require('fs')
//const input = fs.readFileSync('/dev/stdin', 'utf-8')
const [A, B, C] = input_2760.split("\n")

console.log(`${A}${B}${C}`)
console.log(`${B}${C}${A}`)
console.log(`${C}${B}${A}`)
console.log(`${A.substring(0,10)}${B.substring(0,10)}${C.substring(0,10)}`)