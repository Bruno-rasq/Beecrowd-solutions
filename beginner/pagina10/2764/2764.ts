const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.trim().split('\n')

lines.forEach(line => {
    let [dd, mm, yy] = line.split('/')
    console.log(`${mm}/${dd}/${yy}`)
    console.log(`${yy}/${mm}/${dd}`)
    console.log(`${dd}-${mm}-${yy}`)
})