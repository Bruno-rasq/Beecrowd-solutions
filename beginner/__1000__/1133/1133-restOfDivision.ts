const input = 
`8
1`

const lines = input.split('\n');

let X = Number(lines.shift());
let Y = Number(lines.shift());

function Main(num1: number, num2: number): void {
    
    let values = [num1, num2]
    let order = [...values].sort((a, b) => a - b);

    let arr: number[] = []
    for(let i = order[0] + 1; i < order[1]; i++){
        if( i % 5 > 1 && i % 5 < 4 ){
            arr.push(i)
        }
    }

    arr.forEach(el => console.log(el))
}

Main(X, Y)