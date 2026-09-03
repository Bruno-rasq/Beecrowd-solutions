const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n')
const n = Number(lines.shift())

for(let i = 0; i < n; i++){

    let curr = lines.shift()
    let result = []

    for(let j = 0; j < curr.length; j++){
        if(curr[j] != curr[j].toUpperCase()){
            result.unshift(curr[j])
        }
    }

    console.log(result.join(""))
}