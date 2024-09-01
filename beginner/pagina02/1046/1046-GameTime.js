// let input = require('fs').readFileSync("./test/stdin", 'utf8');
// let lines = input.split('\n');

console.log(" 1046 - Game Time ");

const input = `1 0`;

let lines = input.split(' ');
let [ a, b ] = lines

a = Number(a)
b = Number(b)

if( a > b ){
    let resp = (24 - a) + b;
    console.log(`O JOGO DUROU ${resp} HORA(S)`)

} else if ( a < b ){
    let resp = b - a;
    console.log(`O JOGO DUROU ${resp} HORA(S)`)

} else if ( a == b){
    let resp = (24 - a) + b;
    console.log(`O JOGO DUROU ${resp} HORA(S)`)
};