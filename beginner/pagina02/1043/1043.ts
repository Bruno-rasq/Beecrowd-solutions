const input = require('fs').readFileSync("./test/stdin", 'utf8');
const lines = input.split(' ');

const A = Number(lines.shift());
const B = Number(lines.shift());
const C = Number(lines.shift());

const perimetro = (A + B + C)
const area = ((A + B) * C ) / 2;
const condicao = A < (B + C) && B < ( A + C) && C < (A + B)

console.log( condicao ? `perimetro = ${perimetro.toFixed(1)}` : `Area = ${area.toFixed(1)}`)