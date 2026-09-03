const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'uft-8')
let [A, B, C] = input.split(" ").map(item => parseFloat(item));

let AreaTring = (A * C) / 2.0;
let circle = parseFloat(3.14159) * Math.pow(C, 2);
let trapezium = ((A + B) * C) / 2.0;
let square = Math.pow(B, 2);
let retangle = A * B;

console.log(`TRIANGULO: ${AreaTring.toFixed(3)}`);
console.log(`CIRCULO: ${circle.toFixed(3)}`);
console.log(`TRAPEZIO: ${trapezium.toFixed(3)}`);
console.log(`QUADRADO: ${square.toFixed(3)}`);
console.log(`RETANGULO: ${retangle.toFixed(3)}`);
