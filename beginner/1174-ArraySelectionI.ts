const input = `0
-5
63
-8.5`

//const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n')

for(let i = 0; i < lines.length - 1; i++){
    let curr = Number(lines[i])

    if (curr <= 10){
        console.log(`A[${i}] = ${curr.toFixed(1)}`)
    }
}