const input = `3
8
51
7
2
0
1`;

//const input = require('fs').readFileSync('/dev/stdin', 'utf8')
const lines = input.split('\n');

namespace OUTPUT {

    export const Is_Prime = (num: number): string => {

        if(num == 0 || num == 1 ) return 'nao eh primo'

        let dividers: number[] = []
        for(let i = num; i > 0; i-- ){
            if(num % i == 0) dividers.push(i)
        }

        return dividers.length == 2 ? 'eh primo' : 'nao eh primo'
    }
}

namespace SETUP {

    export const Setup = (data : string[]): void  => {

       let numbers = data.map(element => Number(element))

       numbers.forEach(num => {

        console.log(`${num} ${OUTPUT.Is_Prime(num)}`)
       })
    }

}


SETUP.Setup(lines)