const input = `5
0 0 1 0 1
6
0 0 0 0 0 1
0`

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n');

namespace ALG {
    export const Head_and_Tail = (games: number, historic: number[]): void => {

        let Mary_wins: number = 0;
        let John_wins: number = 0;

        for(let i = 0; i < games; i++){
            if(historic[i] == 0){
                Mary_wins++
            } else {
                John_wins++
            }
        }
        
        console.log(`Mary won ${Mary_wins} times and John won ${John_wins} times`)
    }
}

namespace SETUP {

    export const setup = (data : string[]): void => {

        for(let i = 0; i < data.length; i+=2){

            let int = Number(data[i])

            if(int === 0) break //EOL

            let gameHistoric: number[] = data[i + 1]
                                        .split(' ')
                                        .map(element => Number(element))

            ALG.Head_and_Tail(int, gameHistoric)
        }
    }
}

SETUP.setup(lines)