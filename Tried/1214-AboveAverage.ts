const input = `5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91`

// const input = require('fs').readFileSync('/dev/stdin', 'utf8')
const lines = input.trim().split('\n')


function above_average(arr: string[]) : void {

    let int = Number(arr.shift())
    
    for(let i = 0; i < int; i++){

        let [ len, ...rest ] = arr[i].split(' ').map(element => Number(element))
        
        let average = (rest.reduce((acc, value) => acc + value, 0) / len)
        let response = 0

        rest.forEach(aluno => {
            if(aluno > average) response += 1
        })

        console.log(`${((response / len) * 100).toFixed(3)}%`)
    }
    
}

above_average(lines)