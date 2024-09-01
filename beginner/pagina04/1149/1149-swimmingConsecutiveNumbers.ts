const input = `3 -1 0 -2 2`

//const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split(' ')


function main(): void {

    let A: number = Number(lines.shift())
    let N: number = 0

    for (let i = 0; i < lines.length; i++) {
        let curr = Number(lines[i])
        if (curr > 0) {
            N = curr
            break
        }
    }

    let response = 0
    for (let j = 0; j < N; j++) {
        response += A + j
    }

    console.log(response)

}

main()