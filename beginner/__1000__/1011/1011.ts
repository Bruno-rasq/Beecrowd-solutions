const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')
const pi = 3.14159

let R = Number(lines[0])

let volume = ((4 / 3.0) * (pi * (R ** 3)))

console.log(`VOLUME = ${volume.toFixed(3)}`)