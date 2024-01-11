const input = `5 2
6 3
5 0`;

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n');

const Sequences_of_numbers_and_sum = (n1: number, n2: number): void => {
    let arrAux: number[] = [n1, n2].sort()

    let response = ''
    let sum = 0
    for(let i = arrAux[0]; i <= arrAux[1]; i++){
        response += ` ${i}`
        sum += i
    }

    console.log(`${response.trim()} Sum=${sum}`)
}

const Setup = (datas: string[]): void => {

   for(let i  = 0; i < datas.length; i++){

        let [ m, n ] = datas[i]
                        .split(' ')
                        .map(e => Number(e))

        if(m == 0 || m < 0 || n == 0 || n < 0) break

        Sequences_of_numbers_and_sum(m, n)
   }
}

Setup(lines)