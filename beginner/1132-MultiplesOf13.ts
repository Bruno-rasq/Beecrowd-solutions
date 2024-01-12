const input = `200
100`;

//const input = require('fs').readFileSync('/dev/stdin', 'utf8')
const lines = input.split('\n').map(element => Number(element));

const divisionBy13 = (ini: number, fin: number): number => {

    let sum: number = 0
    for(let i = ini; i <= fin; ++i){
        if(i % 13 !== 0) sum += i
    }
    return sum
}

const MUL13 = (data : number[]): void  => {

    let [ x, y ] = data
    
    if(x > y){
        [x, y] = [y, x]
    }
    
    console.log(divisionBy13(x, y))
}

MUL13(lines)