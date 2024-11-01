const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')
const n = Number(lines.shift())

let villains = []
for(let i = 0; i < n; i++){
    let villain = lines.shift()

    if(!villains.includes(villain)){
        villains.push(villain)
        console.log("Y")
    } else {
        console.log("N")
    }
}