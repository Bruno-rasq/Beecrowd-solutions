// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split(' ').map((item: string) => Number(item));

let sortedArray = [...lines].sort((a, b) => b - a)


const Main = (arr: number[]): void => {

    let [ a, b, c ] = arr

    let a2 = Math.pow(a, 2) 
    let bc2 = (Math.pow(b, 2) + Math.pow(c, 2))

    let response: string[] = []

    if(a >= (b + c)){
       response.push(`NAO FORMA TRIANGULO`) 

    } else {
        if(a2 === bc2) response.push(`TRIANGULO RETANGULO`)
        if(a2 > bc2) response.push(`TRIANGULO OBTUSANGULO`)
        if(a2 < bc2) response.push(`TRIANGULO ACUTANGULO`)
        if(a === b && b === c) response.push(`TRIANGULO EQUILATERO`)
        if(a !== b ? b === c : b !== c) response.push(`TRIANGULO ISOSCELES`)
    }
    
    console.log(response.join('\n'))
}

Main(sortedArray)