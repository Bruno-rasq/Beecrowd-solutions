const input = `3
11
7
18`
const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')

const Bill = (data: string[]): void => {
    
    let num = Number(data.shift())
    for(let i = 0; i < num; i++){
        let currTest = Number(data[i])
        let response = 0

        for(let j = 0; j < currTest; j++){
            j % 2 == 0 ? response += 1 : response -= 1
        }
        console.log(response)
    }
}

Bill(lines)