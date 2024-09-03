const fs = require('fs')
const input = fs.readFileSync("/dev/stdin", 'utf-8')
const lines = input.split('\n').map(Number)

function main(){

    let int = lines.shift()
    for (let i = 0; i < int; i ++){
        Fib(lines.shift())
    }
}

function Fib(n){
    let first = 0;
    let second = 1;
    let fib = [first, second];

    for (let i = 0; i < n - 1; i ++){
        let curr = first + second
        fib.push(curr)
        first = second
        second = curr
    }

    let response = 0;
    if (n == 1) response = 1
    if (n == 0) response = 0
    else response = fib[fib.length - 1]

    console.log(`Fib(${n}) = ${response}`)
}

main()