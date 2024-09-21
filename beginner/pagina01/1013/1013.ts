const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

let arry: number[] = lines[0].split(' ').map(Number)
let maior = Math.max(...arry)

console.log(`${maior} eh o maior`)