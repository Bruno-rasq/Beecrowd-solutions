const input = `3
8
51
7`;

const lines = input.split('\n').map(element => Number(element))

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n').map(element => Number(element))

namespace SOLUTION {

    export const setup_data = (data: number[]): number[] => {

        let arr: number[] = []
        let integer = Number(data.shift());
        for(let i = 0; i < integer; i++){
            arr.push(data[i])
        }

        return arr
    }

    export const IsPrime = (x: number): string => {

        let divisors = []
        for(let i = x; i > 0; i--){
            if(x % i == 0) divisors.push(i)
        }

        return divisors.length == 2 ? `eh primo` : `nao eh primo`
    }

    export const response = (arr: number[]): void => { 

        arr.forEach(num => {
            console.log(`${num} ${IsPrime(num)}`)
        })
    }
}

SOLUTION.response(SOLUTION.setup_data(lines))