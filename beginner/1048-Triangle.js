let input = require('fs').readFileSync("./test/stdin", 'utf8');
let lines = input.split(' ');

let A = Number(lines.shift());
let B = Number(lines.shift());
let C = Number(lines.shift());

let perimetro = (A + B + C)
let area = ((A + B) * C ) / 2;

if ( A < (B + C) && B < ( A + C) && C < (A + B)){
    console.log(`perimetro = ${perimetro.toFixed(1)}`)

} else {
    console.log(`Area = ${area.toFixed(1)}`)
};

//exem Input : 6.0 4.0 2.1