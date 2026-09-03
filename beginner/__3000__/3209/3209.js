const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf8')
const lines = input.split('\n')
const n = Number(lines.shift())

for(let i = 0; i < n; i++){
    let [t, ...reguas] = lines.shift().split(" ").map(Number)

    let total = reguas[0]

    for(let j = 1; j < t; j++){
        total = (total - 1) + reguas[j]

    }

    console.log(total)
}