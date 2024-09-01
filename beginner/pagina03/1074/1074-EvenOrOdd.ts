const input = `4
-5
0
3
-4`;

//const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n');

// setup data
const data: number[] = Setup(lines)
OUTPUT(data)

function PosNeg(num: number): string {
    if(num > 0){
       return ' positive' 
    }
    return ' negative' 
}

function EvenOdd(n: number){

    let response: string = "";

    if(n == 0) response =  'null'

    else if (n % 2 == 0){
        response =  'even' + PosNeg(n)
    } else {
        response =  'odd' + PosNeg(n)
    }
   
    return response
}

function OUTPUT(arr: number[]): void {
    arr.forEach((num) => {
        console.log(EvenOdd(num).toUpperCase())
    })
}

function Setup(input: string[]): number[]  {
    let int = Number(input.shift())

    let arr: number[] = []
    for(let n  = 0; n < int; n++){
        arr.push(Number(input[n]))
    }

    return arr
}