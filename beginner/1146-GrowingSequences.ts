const input = `5
10
3
0`

//const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n')

for(let i = 0; i < lines.length; i++){
    let output: string[] = []
    let curr = Number(lines[i])

    if(curr === 0) break

    for(let j = 0; j < curr; j++){
        output.push(`${j + 1}`)
    }

    console.log(output.join(' ').trim())
}