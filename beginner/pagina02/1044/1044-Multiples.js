console.log(" 1044 - Multiples ");

const input = `6 25`;

let lines = input.split(' ').map(el => Number(el))
let [ a, b ] = lines

if(a < b){
    [a ,b] = [b ,a]
}

let resp = a % b === 0 ? 'Sao Multiplos' : 'Nao sao Multiplos';
console.log(resp)