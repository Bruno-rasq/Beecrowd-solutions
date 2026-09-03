const input = `3
3 -2
-8 0
0 8`;

const lines = input.split('\n')

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')

namespace SETUP {

    export const setup = (data: string[]): string[] => {

        let arrayAux = []
        let integer = Number(data.shift());
        for(let i = 0; i < integer; i++){
            
            arrayAux.push(data[i])
        }

        return arrayAux
    }
}

namespace SOLUTION {

    export const dividing_y_by_x = (arr: string[]) => {

        arr.forEach((data) => {
            let [x, y] = data.split(' ').map(num => Number(num))

            if(y == 0){
                console.log(`divisao impossivel`)
            } else {
                console.log((x / y).toFixed(1))
            }
        })

    }
}

SOLUTION.dividing_y_by_x(SETUP.setup(lines))