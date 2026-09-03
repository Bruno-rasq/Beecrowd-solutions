const input = `3`
const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')

const Our_days_are_never_comming_back = (data: string[]): void => {
    let quote = `Life is not a problem to be solved, but a reality to be experienced.`
    let num = Number(data.shift())
    let response = ''
    for(let i = 0; i < num; i++){
        response += quote[i].toUpperCase()
    }
    console.log(response)
}

Our_days_are_never_comming_back(lines)