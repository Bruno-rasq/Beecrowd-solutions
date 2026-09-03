const fs = require("fs")
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n').map(Number)

function sum_evens(num: number): number {
    let sum = 0;
    let count = 0;
    while(count < 5){
        if(num % 2 === 0){
            sum += 0;
            count++
        }
        num++
    }
    return sum 
}

function main(): void {
    for(let line of lines){
        if(line === 0) break
        console.log(sum_evens(line))
    }
}

main()