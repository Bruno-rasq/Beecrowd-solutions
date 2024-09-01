const input = `7
4 5
13 10
6 4
3 3
3 5
3 4
3 8`

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n');

namespace ALG {

    export const Sum_consecutives_odds = (arr: number[]): void => {

        let sum: number = 0;
        let [ x, y ] = arr

        for(let i = x + 1; i < y ; i++){
            if(i % 2 !== 0) sum += i
        }

        console.log(sum)
    }
}

namespace SETUP {

    export const trigger = (data: string[]): void => {

        let int = Number(data.shift())

        for(let i = 0; i < int; i++){

            let numbers = data[i]
                        .toString()
                        .split(' ')
                        .map(element => Number(element))
                        .sort((a, b) => a - b)

            ALG.Sum_consecutives_odds(numbers)
        }
    }
}

SETUP.trigger(lines)