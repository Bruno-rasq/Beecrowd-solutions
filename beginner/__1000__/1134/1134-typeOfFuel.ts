//const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n').map((item: string) => Number(item));

const Output = (arr: number[]): void => {

    let response = [
        `MUITO OBRIGADO`,
        `Alcool: ${arr[0]}`,
        `Gasolina: ${arr[1]}`,
        `Diesel: ${arr[2]}`
    ];

    console.log(response.join('\n'))
}

const Input = (arr: number[]): void => {

    let alcool: number = 0
    let gasoline: number = 0
    let diesel: number = 0

    let Condicion: number = 0
    while(Condicion != 4){

        let N = arr.shift()

        if(N === 1) alcool++
        if(N === 2) gasoline++
        if(N === 3) diesel++

        Condicion = Number(N)
        
    }

    Output([alcool, gasoline, diesel])
}

Input(lines)