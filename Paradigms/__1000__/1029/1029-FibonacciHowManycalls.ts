const input = `2
5
4`

//const input = require('fs').readFileSync("/dev/stdin", "utf8");
const lines = input.split('\n');

let calls: number = 0;

function Fib(n: number): number {
    
    if(n === 1 || n === 0) return n
    calls += 2;
    return Fib(n - 1) + Fib(n - 2);
}

function main(): void {

    let int = Number(lines.shift())
    for(let i = 0; i < int; i++){
        let n = Number(lines[i])
        calls = 0;

        let output =  Fib(n)

        console.log(`Fib(${n}) = ${calls} calls = ${output}`)
    }

}

main();