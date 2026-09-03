const input = `5 4
7 2
3 8
2 2`;

const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')

namespace SETUP {

    export const setup = (data: string[]): void => {

        for(let i = 0; i < data.length; i++){
            
            let [x, y] = data[i].split(' ').map(num => Number(num))
            
            if(x == y) {
                break
            } else {
                SOLUTION.Ascendetn_or_Descendent(x, y)
            }
        }
    }
}

namespace SOLUTION {

    export const Ascendetn_or_Descendent = (x: number, y: number) => {

        if(y > x){
            console.log(`Crescente`)
        } else {
            console.log(`Decrescente`)
        }
    }
}


SETUP.setup(lines)  