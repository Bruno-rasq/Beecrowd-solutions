const input = `3
Computers account for only 5% of the country's commercial electricity consumption.
Input
frequency letters`;

//const input = require('fs').readFileSync('/dev/stdin', 'utf8')
const lines = input.split('\n');


namespace SETUP {

    const filter_Letters = (phrase: string) => {

        let arr = phrase.toLowerCase().split('').filter(char => /[a-z]/.test(char))
        
        Solution.letter_frequency(arr)
    }

    export const start = (arr: string[]): void => {

        let int = Number(arr.shift());

        for(let i = 0; i < int; i++){
            let phrase = arr[i]

            filter_Letters(phrase)
        }
    }
}

namespace Solution {

    export const letter_frequency = (arr: string[]) => {

        let frequency =  new Map<string, number>();
        let maior_valor: number = 1

        for(let char of arr){
            frequency.has(char) 
            ? frequency.set(char, frequency.get(char)! + 1) 
            : frequency.set(char, 1)
        }


        frequency.forEach(key => {
            if(key > maior_valor){
                maior_valor = key
            }
        })

        let response: string[] = []
        frequency.forEach((value, key) => {
            if(value >= maior_valor){
                response.push(key)
            }
        })

        console.log(response.sort().join(''))
    }
}

SETUP.start(lines)