const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split("\n")

const [ x1, y1 ] = lines[0].split(' ')
const [ x2, y2 ] = lines[1].split(' ')

let distance = Math.sqrt(
    Math.pow((x2 - x1), 2) +  Math.pow((y2 - y1), 2) 
)

console.log(distance.toFixed(4))