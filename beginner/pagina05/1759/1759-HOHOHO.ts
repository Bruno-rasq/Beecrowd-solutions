// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')
//const n = Number(lines.shift());

const n = 5

function main(num: number): string {
    let response = ''

    for(let i = 1; i <= num; i++){
        if(i == num){
            response += 'Ho!'
        } else {
            response += 'Ho '
        }
    }

    return response
}

console.log(main(n))