const fs = require('fs')
const input = fs.readFileSync('/dev/stdin' , 'utf-8')
const lines = input.split('\n')

const [john, medico] = lines

console.log(john.length >= medico.length ? 'go' : 'no')