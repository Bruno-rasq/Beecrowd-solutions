const [a, b] = require('fs').readFileSync("/dev/stdin", 'utf8').split(" ").map(Number);
let resp;

if( a > b ) resp = (24 - a) + b;
else if ( a < b ) resp = b - a;
else if ( a == b) resp = (24 - a) + b;

console.log(`O JOGO DUROU ${resp} HORA(S)`)