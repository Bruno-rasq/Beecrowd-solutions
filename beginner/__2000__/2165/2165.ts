const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const chars = input.split('').length

console.log(chars <= 141 ? 'TWEET' : 'MUTE')