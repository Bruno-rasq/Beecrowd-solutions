// teste
// const input: string = `-5
// 0
// -3
// -4
// 12`

//const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines: number[] = input.split('\n').map((item) => Number(item));

const output = (arr: number[]): void => {

    let response: string[] = [
        `${arr[0]} valor(es) par(es)`,
        `${arr[1]} valor(es) impar(es)`,
        `${arr[2]} valor(es) positivo(s)`,
        `${arr[3]} valor(es) negativo(s)`
    ] 

    console.log(response.join('\n'))
}
  
const Input = (arr: number[]): void => {

    const values = arr

    let Even: number = 0;
    let Odd: number = 0;
    let Positive: number = 0;
    let Negative: number = 0;

    const Condicion = {
        isEven(value: number){
            value % 2 === 0 ? Even++ : Odd++
        },
        isPositive(value: number){
            value > 0 ? Positive++ : Negative++
        }
    }

    values.forEach((num) => {

        Condicion.isEven(num)
        if(num !== 0) Condicion.isPositive(num)

    })

    output([Even, Odd, Positive, Negative])
}

// Input(lines) Start