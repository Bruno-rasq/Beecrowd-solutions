const input = `4
Hulk 5000
Tony 1000
Thor 50
Steve 500`
const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')

const Mjolnir = (data: string[]): void => {
    
    let num = Number(data.shift())
    for(let i = 0; i < num; i++){
        let [ name, force ] = String(data[i]).split(' ')
        console.log(name === 'Thor' ? 'Y' : 'N')
    }
}

Mjolnir(lines)