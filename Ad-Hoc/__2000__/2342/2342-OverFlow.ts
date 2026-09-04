const input = `323500
42 * 35`
const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')

const OverFlow = (data: string[]): void => {
    let Max_memory = Number(data.shift())
    let calc = eval(String(data.shift()))

    console.log(calc > Max_memory ? 'OVERFLOW' : 'OK')
    
}

OverFlow(lines)