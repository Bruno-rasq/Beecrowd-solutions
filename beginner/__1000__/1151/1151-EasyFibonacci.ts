const input = `5`;

const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')

namespace SOLUTION {

    export const Fibonacci = (x: number): number[] => {

        let fibonacci: number[] = [0, 1]

        for(let i = 2; i < x; i++){
            fibonacci.push(fibonacci[i - 1] + fibonacci[i - 2])
        }

        return fibonacci
    }

    export const solution = (arr: number[], n: number): void => {

        let response = []
        for(let i = 0; i < n; i++){
            response.push(arr[i])
        }
        console.log(response.join(' '))
    }
}

let N = Number(lines.shift())

SOLUTION.solution(SOLUTION.Fibonacci(N), N)