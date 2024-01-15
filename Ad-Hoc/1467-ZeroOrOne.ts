const input = `1 1 0
0 0 0
1 0 0
1 1 1`

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n');


namespace ALG {

    export const zero_or_one_response = (arr: number[]): void => {

        let [ A, B, C ] = arr 
        
        if( A == B && C == B) console.log('*') 
        if( A == B && C != B) console.log('C')
        if( A == C && B != C) console.log('B')
        if( B == C && A != C) console.log('A')
        
    }
}

namespace SETUP {

    export const setup = (data : string[]): void => {

        for(let i = 0; i < data.length - 1; i++){

            let game = data[i].split(' ').map(element => Number(element))

            ALG.zero_or_one_response(game)
        }
    }
}

SETUP.setup(lines)